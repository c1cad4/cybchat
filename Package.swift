// swift-tools-version: 5.9

import PackageDescription

let package = Package(
    name: "cybchat",
    platforms: [
        .iOS(.v16),
        .macOS(.v13)
    ],
    products: [
        .executable(
            name: "cybchat",
            targets: ["cybchat"]
        ),
    ],
    targets: [
        .executableTarget(
            name: "cybchat",
            path: "cybchat",
            exclude: [
                "Info.plist",
                "Assets.xcassets",
                "cybchat.entitlements",
                "cybchat-macOS.entitlements",
                "LaunchScreen.storyboard"
            ]
        ),
    ]
)