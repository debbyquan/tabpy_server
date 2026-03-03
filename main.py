import os
import sys
from tabpy.tabpy_server.app.app import TabPyApp

def main():
    """Start TabPy server configured for Railway"""
    
    # Railway automatically sets the PORT environment variable
    port = int(os.environ.get('PORT', 9004))
    
    print("🚀 Starting TabPy Server for Railway...")
    print(f"📡 Port: {port}")
    print(f"🌐 Host: 0.0.0.0 (Railway requirement)")
    
    try:
        # Create TabPy application instance
        app = TabPyApp()
        
        # Start the server
        # Railway requires host='0.0.0.0' to accept external connections
        app.run(
            host='0.0.0.0',
            port=port,
            debug=False  # Set to False for production
        )
        
    except Exception as e:
        print(f"❌ Error starting TabPy server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
