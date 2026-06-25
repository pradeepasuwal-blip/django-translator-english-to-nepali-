<!DOCTYPE html>
<html>
<head>
  <title>Django English to Nepali Translator</title>
</head>
<body>
  <h1>Django English to Nepali Translator</h1>

  <h2>Overview</h2>
  <p>
    This project is a simple Django web application that translates text from English to Nepali. 
    It supports both a web interface (HTML form) and a REST API endpoint for programmatic access. 
    The translation is powered by the <strong>deep_translator</strong> library.
  </p>

  <h2>Features</h2>
  <ul>
    <li>Web form for users to input English text and view Nepali translation.</li>
    <li>REST API endpoint (<code>/api/translate/</code>) that returns JSON responses.</li>
    <li>Built with Django and Django REST Framework.</li>
  </ul>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.10+</li>
    <li>Django</li>
    <li>djangorestframework</li>
    <li>deep-translator</li>
  </ul>

  <h3>Install dependencies:</h3>
  <pre><code>pip install django djangorestframework deep-translator</code></pre>

  <h2>Setup</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/your-username/django-translator.git
cd django-translator</code></pre>
    </li>
    <li>Run migrations:
      <pre><code>python manage.py migrate</code></pre>
    </li>
    <li>Start the development server:
      <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>Open your browser at:
      <ul>
        <li><a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> → Web form translator.</li>
        <li><a href="http://127.0.0.1:8000/api/translate/">http://127.0.0.1:8000/api/translate/</a> → REST API endpoint.</li>
      </ul>
    </li>
  </ol>

  <h2>Usage</h2>
  <h3>Web Form</h3>
  <p>Enter English text in the form and submit to see Nepali translation displayed on the page.</p>

  <h3>REST API</h3>
  <p>Send a POST request:</p>
  <pre><code>{
  "text": "Hello",
  "target": "ne"
}</code></pre>
  <p>Response:</p>
  <pre><code>{
  "translated": "नमस्ते"
}</code></pre>

  <h2>Project Structure</h2>
  <pre><code>translator/
├── main/
│   ├── views.py        # Contains home and translate_api views
│   ├── urls.py         # Routes for home and API
│   └── templates/
│       └── main/index.html  # Web form template
├── translator/
│   ├── settings.py     # Django settings
│   ├── urls.py         # Project-level URL routing
└── manage.py</code></pre>

  <h2>Future Improvements</h2>
  <ul>
    <li>Add Text-to-Speech output for translations.</li>
    <li>Support multiple source and target languages.</li>
    <li>Improve error handling and validation.</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the MIT License. Feel free to use and modify it.</p>
</body>
</html>
