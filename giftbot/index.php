<!DOCTYPE html>
<html>
<head>
    <title>Easy Gift WebApp</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .case { margin: 10px; padding: 15px; background: #f0f0f0; border-radius: 10px; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>🎁 Easy Gift</h1>
    <p>Выберите кейс:</p>
    <div class="case">
        <h3>Shirl Case</h3>
        <button onclick="openCase('shirl')">Открыть за 10 звёзд</button>
    </div>
    <div class="case">
        <h3>Fetch Case</h3>
        <button onclick="openCase('fetch')">Открыть за 20 звёзд</button>
    </div>
    <script>
        function openCase(caseName) {
            alert(`Вы открыли ${caseName} кейс!`);
            // Здесь будет запрос к вашему боту через Telegram WebApp API
        }
    </script>
</body>
</html>