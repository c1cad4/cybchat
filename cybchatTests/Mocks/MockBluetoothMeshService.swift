//
// MockBluetoothMeshService.swift
// cybchatTests
//
// This is free and unencumbered software released into the public domain.
// For more information, see <https://unlicense.org>
//

import Foundation
import MultipeerConnectivity
@testable import cybchat

class MockBluetoothMeshService: BluetoothMeshService {
    var sentMessages: [(message: CybchatMessage, packet: CybchatPacket)] = []
    var sentPackets: [CybchatPacket] = []
    var connectedPeers: Set<String> = []
    var messageDeliveryHandler: ((CybchatMessage) -> Void)?
    var packetDeliveryHandler: ((CybchatPacket) -> Void)?
    
    // Override these properties
    var mockNickname: String = "MockUser"
    
    override var myPeerID: String {
        didSet {
            // Update when changed
        }
    }
    
    var nickname: String {
        return mockNickname
    }
    
    var peerID: String {
        return myPeerID
    }
    
    override init() {
        super.init()
        self.myPeerID = "MOCK1234"
    }
    
    func simulateConnectedPeer(_ peerID: String) {
        connectedPeers.insert(peerID)
        delegate?.didConnectToPeer(peerID)
        delegate?.didUpdatePeerList(Array(connectedPeers))
    }
    
    func simulateDisconnectedPeer(_ peerID: String) {
        connectedPeers.remove(peerID)
        delegate?.didDisconnectFromPeer(peerID)
        delegate?.didUpdatePeerList(Array(connectedPeers))
    }
    
    override func sendMessage(_ content: String, mentions: [String], to room: String? = nil, messageID: String? = nil, timestamp: Date? = nil) {
        let message = CybchatMessage(
            id: messageID ?? UUID().uuidString,
            sender: mockNickname,
            content: content,
            timestamp: timestamp ?? Date(),
            isRelay: false,
            originalSender: nil,
            isPrivate: false,
            recipientNickname: nil,
            senderPeerID: myPeerID,
            mentions: mentions.isEmpty ? nil : mentions
        )
        
        if let payload = message.toBinaryPayload() {
            let packet = CybchatPacket(
                type: 0x01,
                senderID: myPeerID.data(using: .utf8)!,
                recipientID: nil,
                timestamp: UInt64(Date().timeIntervalSince1970 * 1000),
                payload: payload,
                signature: nil,
                ttl: 3
            )
            
            sentMessages.append((message, packet))
            sentPackets.append(packet)
            
            // Simulate local echo
            DispatchQueue.main.async { [weak self] in
                self?.delegate?.didReceiveMessage(message)
            }
            
            // Call delivery handler if set
            messageDeliveryHandler?(message)
        }
    }
    
    override func sendPrivateMessage(_ content: String, to recipientPeerID: String, recipientNickname: String, messageID: String? = nil) {
        let message = CybchatMessage(
            id: messageID ?? UUID().uuidString,
            sender: mockNickname,
            content: content,
            timestamp: Date(),
            isRelay: false,
            originalSender: nil,
            isPrivate: true,
            recipientNickname: recipientNickname,
            senderPeerID: myPeerID,
            mentions: nil
        )
        
        if let payload = message.toBinaryPayload() {
            let packet = CybchatPacket(
                type: 0x01,
                senderID: myPeerID.data(using: .utf8)!,
                recipientID: recipientPeerID.data(using: .utf8)!,
                timestamp: UInt64(Date().timeIntervalSince1970 * 1000),
                payload: payload,
                signature: nil,
                ttl: 3
            )
            
            sentMessages.append((message, packet))
            sentPackets.append(packet)
            
            // Simulate local echo
            DispatchQueue.main.async { [weak self] in
                self?.delegate?.didReceiveMessage(message)
            }
            
            // Call delivery handler if set
            messageDeliveryHandler?(message)
        }
    }
    
    func simulateIncomingMessage(_ message: CybchatMessage) {
        delegate?.didReceiveMessage(message)
    }
    
    func simulateIncomingPacket(_ packet: CybchatPacket) {
        // Process through the actual handling logic
        if let message = CybchatMessage.fromBinaryPayload(packet.payload) {
            delegate?.didReceiveMessage(message)
        }
        packetDeliveryHandler?(packet)
    }
    
    func getConnectedPeers() -> [String] {
        return Array(connectedPeers)
    }
}