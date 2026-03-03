import os
import sys

print("🚀 Starting TabPy with direct import...")

# Get Railway port
port = int(os.environ.get('PORT', 9004))
print(f"📡 Port: {port}")

try:
    # Import TabPy directly and start it
    from tabpy.tabpy_server.app.app import TabPyApp
    
    print("💻 Creating TabPy app...")
    
    # Try without config file first (older versions)
    try:
        app = TabPyApp()
    except TypeError:
        # If config file required, create minimal one
        print("📋 Creating config file...")
        
        import tempfile
        config_content = f'''[TabPy]
TABPY_PORT = {port}
TABPY_QUERY_OBJECT_PATH = /tmp/query_objects
TABPY_STATE_PATH = /tmp/tabpy

[logging]
TABPY_LOG_LEVEL = INFO
'''
        
        config_file = '/tmp/tabpy_config.conf'
        with open(config_file, 'w') as f:
            f.write(config_content)
        
        app = TabPyApp(config_file=config_file)
    
    print(f"🌐 Starting server on 0.0.0.0:{port}")
    
    # Start the server
    app.run(host='0.0.0.0', port=port, debug=False)
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 TabPy not installed properly")
    sys.exit(1)
    
except Exception as e:
    print(f"❌ Startup error: {e}")
    sys.exit(1)
