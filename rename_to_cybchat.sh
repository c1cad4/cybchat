#!/bin/bash

echo "🔄 Заменяю все упоминания 'bitchat' на 'cybchat'..."

# Исключаем .git, xcodegen и временные файлы
find . -type f \( -name "*.swift" -o -name "*.plist" -o -name "*.md" -o -name "*.yml" -o -name "*.json" -o -name "*.storyboard" \) \
    ! -path "./.git/*" \
    ! -path "./xcodegen/*" \
    ! -name "*.tar.gz" \
    ! -name "*.zip" \
    -exec sed -i '' 's/bitchat/cybchat/g' {} \;

echo "✅ Замена завершена!"

# Проверяем, что замена прошла успешно
echo "🔍 Проверяем результат..."
grep -r "bitchat" . --exclude-dir=.git --exclude-dir=xcodegen --exclude="*.tar.gz" --exclude="*.zip" | head -10

echo "🎉 Готово! Все упоминания 'bitchat' заменены на 'cybchat'" 