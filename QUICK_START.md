# 🚀 CybChat - Быстрый старт

## 📱 Что это?
CybChat - децентрализованное приложение для обмена сообщениями через Bluetooth mesh сеть. Без интернета, без серверов, без номеров телефонов.

## ⚡ Быстрый запуск

### 1. Открыть в Xcode
```bash
cd cybchat-final
open cybchat.xcodeproj
```

### 2. Выбрать target
- **iOS**: `cybchat_iOS` 
- **macOS**: `cybchat_macOS`

### 3. Выбрать устройство
- **iOS**: Подключенный iPhone/iPad (не симулятор!)
- **macOS**: "My Mac"

### 4. Запустить
Нажать ▶️ (Run) в Xcode

## 🔧 Альтернативные способы запуска

### Через XcodeGen
```bash
./xcodegen/bin/xcodegen generate
open cybchat.xcodeproj
```

### Через Just (macOS)
```bash
just run     # Собрать и запустить
just build   # Только собрать
just clean   # Очистить
```

## ⚠️ Важно
- **Требуется физическое устройство** - симулятор не поддерживает Bluetooth
- **Разрешите Bluetooth** при первом запуске
- **iOS 16.0+ / macOS 13.0+**

## 🎯 Функции
- 🔵 Mesh сеть через Bluetooth LE
- 🔵 Шифрование end-to-end
- 🔵 Команды в стиле IRC (/slap, /msg, /who)
- 🔵 Работает офлайн
- 🔵 Экстренное удаление данных (тройной тап)

## 📁 Структура проекта
```
cybchat-final/
├── cybchat/                    # Основной код приложения
├── cybchatShareExtension/      # Расширение для шаринга
├── cybchat.xcodeproj/          # Xcode проект
├── project.yml                 # Конфигурация проекта
├── Package.swift              # Swift Package Manager
└── README.md                  # Подробная документация
```

## 🎨 Новый дизайн
- 🌟 Космический глаз с зеленым центром
- 🌌 Темный космический фон
- ⚪ Белая овальная рамка
- ✨ Эффекты свечения

**Готово к использованию!** 🚀 