#!/bin/bash
source venv/bin/activate
echo "🚀 Starting FastAPI server..."
echo "📖 Open http://127.0.0.1:8000/docs in your browser"
echo "⏹️  Press Ctrl+C to stop"
echo ""
uvicorn main:app --reload
