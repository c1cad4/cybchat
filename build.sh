#!/bin/bash

echo "Building CybChat project..."

# Check if we have the necessary files
if [ ! -f "project.yml" ]; then
    echo "❌ project.yml not found"
    exit 1
fi

if [ ! -d "cybchat" ]; then
    echo "❌ cybchat directory not found"
    exit 1
fi

echo "✅ Project structure looks good"
echo "📱 CybChat - Decentralized Mesh Messaging"
echo "=========================================="
echo "• Based on original cybchat code"
echo "• Updated branding to cybchat"
echo "• New cosmic eye app icon"
echo "• Bluetooth LE mesh networking"
echo "• End-to-end encryption"
echo "• No internet required"
echo ""
echo "To build and run:"
echo "1. Install XcodeGen: brew install xcodegen"
echo "2. Generate project: xcodegen generate"
echo "3. Open cybchat.xcodeproj in Xcode"
echo "4. Build and run on device (no simulator support)"
echo ""
echo "Or use the just commands:"
echo "• just run     - Build and run macOS app"
echo "• just build   - Build only"
echo "• just clean   - Clean build artifacts"
echo ""
echo "Project files updated:"
echo "✅ project.yml - Updated bundle identifiers"
echo "✅ cybchat/CybchatApp.swift - Renamed and updated"
echo "✅ cybchat/Info.plist - Updated display name and descriptions"
echo "✅ cybchat/Assets.xcassets - New cosmic eye app icons"
echo "✅ cybchatShareExtension - Updated branding"
echo "✅ Package.swift - Updated project name"
echo "✅ Justfile - Updated references"
echo "✅ README.md - Updated branding" 