#!/bin/bash
echo "🚀 Setting up Tech Products API..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo ""
echo "✅ Setup complete!"
echo "📝 To start the server, run: ./start.sh"
