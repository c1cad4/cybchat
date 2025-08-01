<img width="256" height="256" alt="icon_128x128@2x" src="https://github.com/user-attachments/assets/90133f83-b4f6-41c6-aab9-25d0859d2a47" />

# cybchat

A decentralized peer-to-peer messaging app that works over Bluetooth mesh networks. No internet required, no servers, no phone numbers. It's the side-groupchat.

cybchat.free

📲 App Store

Warning

Private messages have not received external security review and may contain vulnerabilities. Do not use for sensitive use cases, and do not rely on its security until it has been reviewed. Now uses the Noise Protocol for identity and encryption. Public local chat (the main feature) has no security concerns.

## License

This project is released into the public domain. See the LICENSE file for details.

## Features

* **Decentralized Mesh Network**: Automatic peer discovery and multi-hop message relay over Bluetooth LE
* **Privacy First**: No accounts, no phone numbers, no persistent identifiers
* **Cover Traffic**: Timing obfuscation and dummy messages for enhanced privacy
* **Private Message End-to-End Encryption**: Noise Protocol
* **Store & Forward**: Messages cached for offline peers and delivered when they reconnect
* **IRC-Style Commands**: Familiar `/slap`, `/msg`, `/who` style interface
* **Universal App**: Native support for iOS and macOS
* **Emergency Wipe**: Triple-tap to instantly clear all data
* **Performance Optimizations**: LZ4 message compression, adaptive battery modes, and optimized networking

## Technical Architecture

### Binary Protocol

cybchat uses an efficient binary protocol optimized for Bluetooth LE:

* Compact packet format with 1-byte type field
* TTL-based message routing (max 7 hops)
* Automatic fragmentation for large messages
* Message deduplication via unique IDs

### Mesh Networking

* Each device acts as both client and peripheral
* Automatic peer discovery and connection management
* Store-and-forward for offline message delivery
* Adaptive duty cycling for battery optimization

For detailed protocol documentation, see the Technical Whitepaper.

## Setup

### Option 1: Using XcodeGen (Recommended)

1. Install XcodeGen if you haven't already:  
brew install xcodegen
2. Generate the Xcode project:  
cd cybchat  
xcodegen generate
3. Open the generated project:  
open cybchat.xcodeproj

### Option 2: Using Swift Package Manager

1. Open the project in Xcode:  
cd cybchat  
open Package.swift
2. Select your target device and run

### Option 3: Manual Xcode Project

1. Open Xcode and create a new iOS/macOS App
2. Copy all Swift files from the `cybchat` directory into your project
3. Update Info.plist with Bluetooth permissions
4. Set deployment target to iOS 16.0 / macOS 13.0

### Option 4: just

Want to try this on macos: `just run` will set it up and run from source. Run `just clean` afterwards to restore things to original state for mobile app building and development.

## About

 bluetooth mesh chat, IRC vibes
