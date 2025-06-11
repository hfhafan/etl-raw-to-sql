#!/usr/bin/env python3
"""
ETL Raw Data to SQL - Main Application
Sample/Demo version untuk menunjukkan konsep arsitektur sistem
"""

import os
import sys
import time
import threading
import queue
import logging
from datetime import datetime
from pathlib import Path

# GUI Framework
try:
    import dearpygui.dearpygui as dpg
except ImportError:
    print("DearPyGUI not installed. Please install: pip install dearpygui")
    sys.exit(1)

# Data Processing
try:
    import pandas as pd
except ImportError:
    print("Pandas not installed. Please install: pip install pandas")
    sys.exit(1)

# Import internal modules
from config.app_config import AppConfig
from auth.authentication import AuthenticationManager
from modules.data_processor import DataProcessor
from modules.database_manager import DatabaseManager
from modules.gui_manager import GUIManager

class ETLApplication:
    """Main ETL Application Class"""
    
    def __init__(self):
        self.config = AppConfig()
        self.auth_manager = AuthenticationManager()
        self.data_processor = DataProcessor()
        self.db_manager = DatabaseManager()
        self.gui_manager = GUIManager()
        
        # Application state
        self.is_running = False
        self.current_user = None
        self.processing_queue = queue.Queue()
        self.log_queue = queue.Queue()
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """Setup application logging"""
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(f'logs/app_{datetime.now().strftime("%Y%m%d")}.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def authenticate_user(self):
        """Handle user authentication"""
        try:
            # Show login dialog
            user_credentials = self.gui_manager.show_login_dialog()
            
            if user_credentials:
                # Validate credentials
                user = self.auth_manager.authenticate(
                    user_credentials['username'],
                    user_credentials['password']
                )
                
                if user:
                    self.current_user = user
                    self.logger.info(f"User {user['username']} logged in successfully")
                    return True
                else:
                    self.gui_manager.show_error("Authentication failed")
                    return False
            
            return False
            
        except Exception as e:
            self.logger.error(f"Authentication error: {e}")
            return False
    
    def initialize_application(self):
        """Initialize application components"""
        try:
            # Initialize configuration
            self.config.load_config()
            
            # Initialize database connection
            if not self.db_manager.initialize_connection():
                raise Exception("Database connection failed")
            
            # Initialize GUI
            self.gui_manager.initialize_gui()
            
            # Setup event handlers
            self.setup_event_handlers()
            
            self.logger.info("Application initialized successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Application initialization failed: {e}")
            return False
    
    def setup_event_handlers(self):
        """Setup GUI event handlers"""
        # File processing events
        self.gui_manager.set_file_process_callback(self.process_files)
        
        # Database events
        self.gui_manager.set_db_connect_callback(self.connect_database)
        
        # Export events
        self.gui_manager.set_export_callback(self.export_data)
        
        # Application events
        self.gui_manager.set_exit_callback(self.exit_application)
    
    def process_files(self, file_paths, network_type):
        """Process selected files"""
        try:
            self.logger.info(f"Starting file processing: {len(file_paths)} files")
            
            # Add to processing queue
            for file_path in file_paths:
                self.processing_queue.put({
                    'file_path': file_path,
                    'network_type': network_type,
                    'timestamp': datetime.now()
                })
            
            # Start processing thread
            processing_thread = threading.Thread(
                target=self.process_files_worker,
                daemon=True
            )
            processing_thread.start()
            
        except Exception as e:
            self.logger.error(f"File processing error: {e}")
            self.gui_manager.show_error(f"Processing error: {e}")
    
    def process_files_worker(self):
        """Worker thread for file processing"""
        while not self.processing_queue.empty():
            try:
                task = self.processing_queue.get()
                
                # Update GUI progress
                self.gui_manager.update_progress(f"Processing {task['file_path']}")
                
                # Process file
                result = self.data_processor.process_file(
                    task['file_path'],
                    task['network_type']
                )
                
                if result['success']:
                    # Upload to database
                    upload_result = self.db_manager.upload_data(
                        result['data'],
                        task['network_type']
                    )
                    
                    if upload_result['success']:
                        self.gui_manager.update_progress(
                            f"Successfully processed {task['file_path']}"
                        )
                    else:
                        raise Exception(f"Upload failed: {upload_result['error']}")
                else:
                    raise Exception(f"Processing failed: {result['error']}")
                
                self.processing_queue.task_done()
                
            except Exception as e:
                self.logger.error(f"Worker thread error: {e}")
                self.gui_manager.show_error(f"Processing error: {e}")
    
    def connect_database(self):
        """Handle database connection"""
        try:
            connection_params = self.gui_manager.get_db_connection_params()
            
            if self.db_manager.test_connection(connection_params):
                self.gui_manager.show_success("Database connected successfully")
                return True
            else:
                self.gui_manager.show_error("Database connection failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Database connection error: {e}")
            return False
    
    def export_data(self, export_params):
        """Handle data export"""
        try:
            self.logger.info("Starting data export")
            
            # Get data from database
            data = self.db_manager.get_data_for_export(export_params)
            
            if data is not None:
                # Export data
                export_result = self.data_processor.export_data(
                    data,
                    export_params['format'],
                    export_params['destination']
                )
                
                if export_result['success']:
                    self.gui_manager.show_success("Data exported successfully")
                else:
                    raise Exception(export_result['error'])
            else:
                raise Exception("No data available for export")
                
        except Exception as e:
            self.logger.error(f"Export error: {e}")
            self.gui_manager.show_error(f"Export error: {e}")
    
    def run(self):
        """Main application run method"""
        try:
            # Authenticate user
            if not self.authenticate_user():
                self.logger.info("Authentication failed or cancelled")
                return
            
            # Initialize application
            if not self.initialize_application():
                self.logger.error("Application initialization failed")
                return
            
            # Set running flag
            self.is_running = True
            
            # Start main GUI loop
            self.logger.info("Starting main application loop")
            self.gui_manager.run_main_loop()
            
        except KeyboardInterrupt:
            self.logger.info("Application interrupted by user")
        except Exception as e:
            self.logger.error(f"Application runtime error: {e}")
        finally:
            self.cleanup()
    
    def exit_application(self):
        """Clean exit application"""
        try:
            self.logger.info("Exiting application")
            
            # Stop processing
            self.is_running = False
            
            # Close database connections
            self.db_manager.close_connections()
            
            # Cleanup GUI
            self.gui_manager.cleanup()
            
            # Log user logout
            if self.current_user:
                self.logger.info(f"User {self.current_user['username']} logged out")
            
        except Exception as e:
            self.logger.error(f"Exit cleanup error: {e}")
        finally:
            sys.exit(0)
    
    def cleanup(self):
        """Cleanup resources"""
        try:
            # Wait for processing queue to finish
            if not self.processing_queue.empty():
                self.logger.info("Waiting for processing queue to finish...")
                self.processing_queue.join()
            
            # Close all connections
            self.db_manager.close_connections()
            
            self.logger.info("Cleanup completed")
            
        except Exception as e:
            self.logger.error(f"Cleanup error: {e}")

def main():
    """Main function"""
    print("=" * 60)
    print("ETL Raw Data to SQL - Sample/Demo Version")
    print("=" * 60)
    
    # Ensure required directories exist
    os.makedirs('logs', exist_ok=True)
    os.makedirs('config', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Create and run application
    app = ETLApplication()
    app.run()

if __name__ == "__main__":
    main() 