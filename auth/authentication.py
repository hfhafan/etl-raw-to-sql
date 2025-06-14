# Authentication Module - Sample Version
"""
Authentication Module - Sample/Demo Version
Handles user authentication and authorization without exposing production details
"""

import hashlib
import json
import os
from datetime import datetime, timedelta
import logging
import platform
import uuid

class AuthenticationManager:
    """Manages user authentication and session"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.session_timeout = timedelta(hours=8)
        self.active_sessions = {}
        self.users_db = self.load_user_database()
    
    def load_user_database(self):
        """Load user database - simplified for demo"""
        # Create sample users for demo
        return {
            "admin": {
                "username": "admin",
                "password_hash": self.hash_password("admin123"),
                "role": "administrator",
                "permissions": ["read", "write", "admin"]
            },
            "user": {
                "username": "user", 
                "password_hash": self.hash_password("user123"),
                "role": "user",
                "permissions": ["read", "write"]
            }
        }
    
    def hash_password(self, password):
        """Hash password securely"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, username, password):
        """Authenticate user credentials"""
        try:
            if username not in self.users_db:
                return None
            
            user = self.users_db[username]
            password_hash = self.hash_password(password)
            
            if user['password_hash'] == password_hash:
                session_id = self.create_session(user)
                return {
                    'username': user['username'],
                    'role': user['role'],
                    'permissions': user['permissions'],
                    'session_id': session_id
                }
            return None
            
        except Exception as e:
            self.logger.error(f"Authentication error: {e}")
            return None
    
    def create_session(self, user):
        """Create user session"""
        session_id = hashlib.md5(
            f"{user['username']}{datetime.now().isoformat()}".encode()
        ).hexdigest()
        
        self.active_sessions[session_id] = {
            'username': user['username'],
            'created_at': datetime.now(),
            'expires_at': datetime.now() + self.session_timeout,
            'role': user['role']
        }
        return session_id
    
    def validate_session(self, session_id):
        """Validate user session"""
        if session_id not in self.active_sessions:
            return False
        
        session = self.active_sessions[session_id]
        if datetime.now() > session['expires_at']:
            del self.active_sessions[session_id]
            return False
        
        return True
    
    def get_device_id(self):
        """Get unique device identifier - simplified version"""
        try:
            system_info = f"{platform.node()}-{platform.system()}"
            device_id = hashlib.md5(system_info.encode()).hexdigest()
            return device_id
        except Exception as e:
            self.logger.error(f"Error generating device ID: {e}")
            return str(uuid.uuid4())
    
    def is_device_authorized(self, device_id):
        """Check if device is authorized - simplified for demo"""
        # In demo version, all devices are auto-authorized
        return True
    
    def logout(self, session_id):
        """Logout user and destroy session"""
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
            return True
        return False
