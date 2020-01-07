{"changed":true,"filter":false,"title":"settings.py","tooltip":"/retro_jerseys/settings.py","value":"\"\"\"\nDjango settings for retro_jerseys project.\nGenerated by 'django-admin startproject' using Django 1.11.24.\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\nimport dj_database_url\n\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = os.environ.get(\"SECRET_KEY\")\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\n\n\n\n\nALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'),\n                \"260707a982834681b208bb180f93c561.vfs.cloud9.eu-west-1.amazonaws.com\",\n                \"https://liams-the-store.herokuapp.com/\",\n                \"liams-the-store.herokuapp.com\"]\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'django_forms_bootstrap',\n    'accounts',\n    'home',\n    'templates',\n    'products',\n    'checkout',\n    'contact',\n    'cart',\n    'storages',\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n\n]\n\nROOT_URLCONF = 'retro_jerseys.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [os.path.join(BASE_DIR, 'templates')],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n                'django.template.context_processors.media',\n                'cart.contexts.cart_contents',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'retro_jerseys.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\n#DATABASES = {\n #   'default': {\n  #      'ENGINE': 'django.db.backends.sqlite3',\n   #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n   #}\n#}\n\n\nif \"DATABASE_URL\"  in os.environ:\n    DATABASES = {\"default\": dj_database_url.parse(os.environ.get('DATABASE_URL')) }\nelse:\n    print(\"Databas Url not found. Using SQLite instead\")\n    DATABASES = {    \n        'default': {\n            'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n        }\n    }\n\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\nAUTHENTICATION_BACKENDS= [\n    'django.contrib.auth.backends.ModelBackend',\n    'accounts.backends.EmailAuth']\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nAWS_S3_OBJECT_PARAMETERS={\n    'Expires':'Thu, 31st Dec 2099 00:00:01 GMT',\n    'CacheControl':'max-age=94608000',\n    \n}\n\nAWS_STORAGE_BUCKET_NAME='liams-ecommerce-store'\nAWS_S3_REGION_NAME=\"eu-west-1\"\nAWS_ACCESS_KEY_ID=os.environ.get(\"AWS_ACCESS_KEY_ID\")\nAWS_SECRET_ACCESS_KEY= os.environ.get(\"AWS_SECRET_ACCESS_KEY\")\n\nAWS_S3_CUSTOM_DOMAIN='liams-ecommerce-store.s3.amazonaws.com'\nSTATICFILES_STORAGE='custom_storages.StaticStorage'\n\n\nSTATICFILES_LOCATION = 'static'\n\nSTATIC_URL = '/static/'\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, \"static\"),\n)\n\nMEDIAFILES_LOCATION = 'media'\nDEFAULT_FILE_STORAGE='custom_storages.MediaStorage'\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'img')\nMEDIA_URL = \"https://liams-ecommerce-store.s3.amazonaws.com/media/\"\n\nSTRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')\nSTRIPE_SECRET = os.getenv('STRIPE_SECRET')\n\n\nMESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'","undoManager":{"mark":99,"position":100,"stack":[[{"start":{"row":162,"column":14},"end":{"row":162,"column":15},"action":"remove","lines":["R"],"id":170}],[{"start":{"row":162,"column":14},"end":{"row":162,"column":15},"action":"insert","lines":["O"],"id":171},{"start":{"row":162,"column":15},"end":{"row":162,"column":16},"action":"insert","lines":["R"]},{"start":{"row":162,"column":16},"end":{"row":162,"column":17},"action":"insert","lines":["E"]}],[{"start":{"row":162,"column":16},"end":{"row":162,"column":17},"action":"remove","lines":["E"],"id":172}],[{"start":{"row":162,"column":16},"end":{"row":162,"column":17},"action":"insert","lines":["A"],"id":173},{"start":{"row":162,"column":17},"end":{"row":162,"column":18},"action":"insert","lines":["G"]},{"start":{"row":162,"column":18},"end":{"row":162,"column":19},"action":"insert","lines":["E"]}],[{"start":{"row":162,"column":19},"end":{"row":162,"column":20},"action":"insert","lines":["="],"id":174}],[{"start":{"row":162,"column":20},"end":{"row":162,"column":22},"action":"insert","lines":["''"],"id":175}],[{"start":{"row":162,"column":21},"end":{"row":162,"column":22},"action":"insert","lines":["s"],"id":176},{"start":{"row":162,"column":22},"end":{"row":162,"column":23},"action":"insert","lines":["t"]},{"start":{"row":162,"column":23},"end":{"row":162,"column":24},"action":"insert","lines":["o"]},{"start":{"row":162,"column":24},"end":{"row":162,"column":25},"action":"insert","lines":["r"]},{"start":{"row":162,"column":25},"end":{"row":162,"column":26},"action":"insert","lines":["a"]}],[{"start":{"row":162,"column":26},"end":{"row":162,"column":27},"action":"insert","lines":["g"],"id":177},{"start":{"row":162,"column":27},"end":{"row":162,"column":28},"action":"insert","lines":["e"]},{"start":{"row":162,"column":28},"end":{"row":162,"column":29},"action":"insert","lines":["s"]},{"start":{"row":162,"column":29},"end":{"row":162,"column":30},"action":"insert","lines":["."]},{"start":{"row":162,"column":30},"end":{"row":162,"column":31},"action":"insert","lines":["b"]},{"start":{"row":162,"column":31},"end":{"row":162,"column":32},"action":"insert","lines":["a"]},{"start":{"row":162,"column":32},"end":{"row":162,"column":33},"action":"insert","lines":["c"]},{"start":{"row":162,"column":33},"end":{"row":162,"column":34},"action":"insert","lines":["k"]},{"start":{"row":162,"column":34},"end":{"row":162,"column":35},"action":"insert","lines":["e"]},{"start":{"row":162,"column":35},"end":{"row":162,"column":36},"action":"insert","lines":["m"]}],[{"start":{"row":162,"column":35},"end":{"row":162,"column":36},"action":"remove","lines":["m"],"id":178}],[{"start":{"row":162,"column":35},"end":{"row":162,"column":36},"action":"insert","lines":["n"],"id":179},{"start":{"row":162,"column":36},"end":{"row":162,"column":37},"action":"insert","lines":["d"]},{"start":{"row":162,"column":37},"end":{"row":162,"column":38},"action":"insert","lines":["s"]},{"start":{"row":162,"column":38},"end":{"row":162,"column":39},"action":"insert","lines":["."]},{"start":{"row":162,"column":39},"end":{"row":162,"column":40},"action":"insert","lines":["b"]},{"start":{"row":162,"column":40},"end":{"row":162,"column":41},"action":"insert","lines":["o"]},{"start":{"row":162,"column":41},"end":{"row":162,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":162,"column":41},"end":{"row":162,"column":42},"action":"remove","lines":["t"],"id":180},{"start":{"row":162,"column":40},"end":{"row":162,"column":41},"action":"remove","lines":["o"]},{"start":{"row":162,"column":39},"end":{"row":162,"column":40},"action":"remove","lines":["b"]}],[{"start":{"row":162,"column":39},"end":{"row":162,"column":40},"action":"insert","lines":["s"],"id":181},{"start":{"row":162,"column":40},"end":{"row":162,"column":41},"action":"insert","lines":["3"]},{"start":{"row":162,"column":41},"end":{"row":162,"column":42},"action":"insert","lines":["b"]},{"start":{"row":162,"column":42},"end":{"row":162,"column":43},"action":"insert","lines":["o"]},{"start":{"row":162,"column":43},"end":{"row":162,"column":44},"action":"insert","lines":["t"]},{"start":{"row":162,"column":44},"end":{"row":162,"column":45},"action":"insert","lines":["o"]}],[{"start":{"row":162,"column":45},"end":{"row":162,"column":46},"action":"insert","lines":["3"],"id":182}],[{"start":{"row":162,"column":46},"end":{"row":162,"column":47},"action":"insert","lines":["."],"id":183},{"start":{"row":162,"column":47},"end":{"row":162,"column":48},"action":"insert","lines":["S"]},{"start":{"row":162,"column":48},"end":{"row":162,"column":49},"action":"insert","lines":["3"]}],[{"start":{"row":162,"column":49},"end":{"row":162,"column":50},"action":"insert","lines":["B"],"id":184},{"start":{"row":162,"column":50},"end":{"row":162,"column":51},"action":"insert","lines":["o"]},{"start":{"row":162,"column":51},"end":{"row":162,"column":52},"action":"insert","lines":["t"]},{"start":{"row":162,"column":52},"end":{"row":162,"column":53},"action":"insert","lines":["o"]},{"start":{"row":162,"column":53},"end":{"row":162,"column":54},"action":"insert","lines":["S"]},{"start":{"row":162,"column":54},"end":{"row":162,"column":55},"action":"insert","lines":["t"]},{"start":{"row":162,"column":55},"end":{"row":162,"column":56},"action":"insert","lines":["o"]},{"start":{"row":162,"column":56},"end":{"row":162,"column":57},"action":"insert","lines":["r"]}],[{"start":{"row":162,"column":57},"end":{"row":162,"column":58},"action":"insert","lines":["a"],"id":185},{"start":{"row":162,"column":58},"end":{"row":162,"column":59},"action":"insert","lines":["g"]},{"start":{"row":162,"column":59},"end":{"row":162,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":162,"column":53},"end":{"row":162,"column":54},"action":"insert","lines":["3"],"id":186}],[{"start":{"row":162,"column":20},"end":{"row":162,"column":62},"action":"remove","lines":["'storages.backends.s3boto3.S3Boto3Storage'"],"id":187},{"start":{"row":162,"column":20},"end":{"row":162,"column":21},"action":"insert","lines":["c"]},{"start":{"row":162,"column":21},"end":{"row":162,"column":22},"action":"insert","lines":["u"]},{"start":{"row":162,"column":22},"end":{"row":162,"column":23},"action":"insert","lines":["s"]},{"start":{"row":162,"column":23},"end":{"row":162,"column":24},"action":"insert","lines":["t"]},{"start":{"row":162,"column":24},"end":{"row":162,"column":25},"action":"insert","lines":["o"]},{"start":{"row":162,"column":25},"end":{"row":162,"column":26},"action":"insert","lines":["m"]},{"start":{"row":162,"column":26},"end":{"row":162,"column":27},"action":"insert","lines":["n"]},{"start":{"row":162,"column":27},"end":{"row":162,"column":28},"action":"insert","lines":["w"]},{"start":{"row":162,"column":28},"end":{"row":162,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":162,"column":28},"end":{"row":162,"column":29},"action":"remove","lines":["e"],"id":188},{"start":{"row":162,"column":27},"end":{"row":162,"column":28},"action":"remove","lines":["w"]},{"start":{"row":162,"column":26},"end":{"row":162,"column":27},"action":"remove","lines":["n"]}],[{"start":{"row":162,"column":26},"end":{"row":162,"column":27},"action":"insert","lines":["_"],"id":189},{"start":{"row":162,"column":27},"end":{"row":162,"column":28},"action":"insert","lines":["s"]},{"start":{"row":162,"column":28},"end":{"row":162,"column":29},"action":"insert","lines":["t"]},{"start":{"row":162,"column":29},"end":{"row":162,"column":30},"action":"insert","lines":["o"]},{"start":{"row":162,"column":30},"end":{"row":162,"column":31},"action":"insert","lines":["a"]},{"start":{"row":162,"column":31},"end":{"row":162,"column":32},"action":"insert","lines":["g"]},{"start":{"row":162,"column":32},"end":{"row":162,"column":33},"action":"insert","lines":["e"]},{"start":{"row":162,"column":33},"end":{"row":162,"column":34},"action":"insert","lines":["e"]},{"start":{"row":162,"column":34},"end":{"row":162,"column":35},"action":"insert","lines":["s"]},{"start":{"row":162,"column":35},"end":{"row":162,"column":36},"action":"insert","lines":["."]},{"start":{"row":162,"column":36},"end":{"row":162,"column":37},"action":"insert","lines":["S"]}],[{"start":{"row":162,"column":37},"end":{"row":162,"column":38},"action":"insert","lines":["t"],"id":190},{"start":{"row":162,"column":38},"end":{"row":162,"column":39},"action":"insert","lines":["a"]},{"start":{"row":162,"column":39},"end":{"row":162,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":162,"column":36},"end":{"row":162,"column":40},"action":"remove","lines":["Stat"],"id":191},{"start":{"row":162,"column":36},"end":{"row":162,"column":49},"action":"insert","lines":["StaticStorage"]}],[{"start":{"row":162,"column":32},"end":{"row":162,"column":33},"action":"remove","lines":["e"],"id":192}],[{"start":{"row":162,"column":30},"end":{"row":162,"column":31},"action":"insert","lines":["r"],"id":193}],[{"start":{"row":162,"column":20},"end":{"row":162,"column":21},"action":"insert","lines":["'"],"id":194}],[{"start":{"row":162,"column":50},"end":{"row":162,"column":51},"action":"insert","lines":["'"],"id":195}],[{"start":{"row":172,"column":29},"end":{"row":173,"column":0},"action":"insert","lines":["",""],"id":196},{"start":{"row":173,"column":0},"end":{"row":173,"column":1},"action":"insert","lines":["D"]},{"start":{"row":173,"column":1},"end":{"row":173,"column":2},"action":"insert","lines":["E"]},{"start":{"row":173,"column":2},"end":{"row":173,"column":3},"action":"insert","lines":["F"]},{"start":{"row":173,"column":3},"end":{"row":173,"column":4},"action":"insert","lines":["A"]},{"start":{"row":173,"column":4},"end":{"row":173,"column":5},"action":"insert","lines":["U"]},{"start":{"row":173,"column":5},"end":{"row":173,"column":6},"action":"insert","lines":["K"]}],[{"start":{"row":173,"column":5},"end":{"row":173,"column":6},"action":"remove","lines":["K"],"id":197}],[{"start":{"row":173,"column":5},"end":{"row":173,"column":6},"action":"insert","lines":["L"],"id":198},{"start":{"row":173,"column":6},"end":{"row":173,"column":7},"action":"insert","lines":["T"]},{"start":{"row":173,"column":7},"end":{"row":173,"column":8},"action":"insert","lines":["_"]},{"start":{"row":173,"column":8},"end":{"row":173,"column":9},"action":"insert","lines":["F"]},{"start":{"row":173,"column":9},"end":{"row":173,"column":10},"action":"insert","lines":["I"]},{"start":{"row":173,"column":10},"end":{"row":173,"column":11},"action":"insert","lines":["L"]},{"start":{"row":173,"column":11},"end":{"row":173,"column":12},"action":"insert","lines":["E"]},{"start":{"row":173,"column":12},"end":{"row":173,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":173,"column":13},"end":{"row":173,"column":14},"action":"insert","lines":["S"],"id":199},{"start":{"row":173,"column":14},"end":{"row":173,"column":15},"action":"insert","lines":["T"]},{"start":{"row":173,"column":15},"end":{"row":173,"column":16},"action":"insert","lines":["O"]},{"start":{"row":173,"column":16},"end":{"row":173,"column":17},"action":"insert","lines":["R"]},{"start":{"row":173,"column":17},"end":{"row":173,"column":18},"action":"insert","lines":["A"]},{"start":{"row":173,"column":18},"end":{"row":173,"column":19},"action":"insert","lines":["T"]},{"start":{"row":173,"column":19},"end":{"row":173,"column":20},"action":"insert","lines":["G"]}],[{"start":{"row":173,"column":19},"end":{"row":173,"column":20},"action":"remove","lines":["G"],"id":200}],[{"start":{"row":173,"column":19},"end":{"row":173,"column":20},"action":"insert","lines":["E"],"id":201}],[{"start":{"row":173,"column":19},"end":{"row":173,"column":20},"action":"remove","lines":["E"],"id":202},{"start":{"row":173,"column":18},"end":{"row":173,"column":19},"action":"remove","lines":["T"]}],[{"start":{"row":173,"column":18},"end":{"row":173,"column":19},"action":"insert","lines":["G"],"id":203},{"start":{"row":173,"column":19},"end":{"row":173,"column":20},"action":"insert","lines":["E"]}],[{"start":{"row":173,"column":20},"end":{"row":173,"column":21},"action":"insert","lines":["="],"id":204}],[{"start":{"row":173,"column":21},"end":{"row":173,"column":23},"action":"insert","lines":["''"],"id":205}],[{"start":{"row":173,"column":22},"end":{"row":173,"column":23},"action":"insert","lines":["c"],"id":206},{"start":{"row":173,"column":23},"end":{"row":173,"column":24},"action":"insert","lines":["u"]},{"start":{"row":173,"column":24},"end":{"row":173,"column":25},"action":"insert","lines":["s"]},{"start":{"row":173,"column":25},"end":{"row":173,"column":26},"action":"insert","lines":["t"]},{"start":{"row":173,"column":26},"end":{"row":173,"column":27},"action":"insert","lines":["o"]},{"start":{"row":173,"column":27},"end":{"row":173,"column":28},"action":"insert","lines":["m"]}],[{"start":{"row":173,"column":22},"end":{"row":173,"column":28},"action":"remove","lines":["custom"],"id":207},{"start":{"row":173,"column":22},"end":{"row":173,"column":37},"action":"insert","lines":["custom_storages"]}],[{"start":{"row":173,"column":37},"end":{"row":173,"column":38},"action":"insert","lines":["."],"id":208},{"start":{"row":173,"column":38},"end":{"row":173,"column":39},"action":"insert","lines":["M"]}],[{"start":{"row":173,"column":39},"end":{"row":173,"column":40},"action":"insert","lines":["d"],"id":209},{"start":{"row":173,"column":40},"end":{"row":173,"column":41},"action":"insert","lines":["i"]},{"start":{"row":173,"column":41},"end":{"row":173,"column":42},"action":"insert","lines":["a"]}],[{"start":{"row":173,"column":41},"end":{"row":173,"column":42},"action":"remove","lines":["a"],"id":210},{"start":{"row":173,"column":40},"end":{"row":173,"column":41},"action":"remove","lines":["i"]},{"start":{"row":173,"column":39},"end":{"row":173,"column":40},"action":"remove","lines":["d"]}],[{"start":{"row":173,"column":39},"end":{"row":173,"column":40},"action":"insert","lines":["e"],"id":211},{"start":{"row":173,"column":40},"end":{"row":173,"column":41},"action":"insert","lines":["d"]},{"start":{"row":173,"column":41},"end":{"row":173,"column":42},"action":"insert","lines":["i"]},{"start":{"row":173,"column":42},"end":{"row":173,"column":43},"action":"insert","lines":["a"]},{"start":{"row":173,"column":43},"end":{"row":173,"column":44},"action":"insert","lines":["S"]}],[{"start":{"row":173,"column":38},"end":{"row":173,"column":44},"action":"remove","lines":["MediaS"],"id":212},{"start":{"row":173,"column":38},"end":{"row":173,"column":50},"action":"insert","lines":["MediaStorage"]}],[{"start":{"row":176,"column":12},"end":{"row":176,"column":21},"action":"remove","lines":["'/media/'"],"id":213},{"start":{"row":176,"column":12},"end":{"row":176,"column":40},"action":"insert","lines":["MEDIA_URL = \"https://%s/%s/\""]}],[{"start":{"row":176,"column":0},"end":{"row":176,"column":12},"action":"remove","lines":["MEDIA_URL = "],"id":214}],[{"start":{"row":176,"column":22},"end":{"row":176,"column":23},"action":"remove","lines":["s"],"id":215},{"start":{"row":176,"column":21},"end":{"row":176,"column":22},"action":"remove","lines":["%"]}],[{"start":{"row":176,"column":21},"end":{"row":176,"column":59},"action":"insert","lines":["liams-ecommerce-store.s3.amazonaws.com"],"id":216}],[{"start":{"row":176,"column":61},"end":{"row":176,"column":62},"action":"remove","lines":["s"],"id":217},{"start":{"row":176,"column":60},"end":{"row":176,"column":61},"action":"remove","lines":["%"]}],[{"start":{"row":176,"column":60},"end":{"row":176,"column":65},"action":"insert","lines":["media"],"id":218}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["#"],"id":221}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["#"],"id":259}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""],"id":284}],[{"start":{"row":28,"column":86},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":285},{"start":{"row":29,"column":0},"end":{"row":29,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":18},"action":"insert","lines":["\"\""],"id":286}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":55},"action":"insert","lines":["https://liams-the-store.herokuapp.com/"],"id":287}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":10},"action":"remove","lines":["import env"],"id":288}],[{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"insert","lines":[","],"id":289}],[{"start":{"row":29,"column":56},"end":{"row":29,"column":57},"action":"insert","lines":[","],"id":290}],[{"start":{"row":29,"column":57},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":291},{"start":{"row":30,"column":0},"end":{"row":30,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":30,"column":16},"end":{"row":30,"column":18},"action":"insert","lines":["\"\""],"id":292}],[{"start":{"row":30,"column":17},"end":{"row":30,"column":46},"action":"insert","lines":["liams-the-store.herokuapp.com"],"id":293}],[{"start":{"row":25,"column":12},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":294},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":28,"column":0},"end":{"row":34,"column":0},"action":"insert","lines":["EMAIL_HOST = 'smtp.zoho.com'","EMAIL_HOST_USER = '############'","EMAIL_HOST_PASSWORD = '##########'","EMAIL_PORT = 587","EMAIL_USE_TLS = True","EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'",""],"id":295}],[{"start":{"row":28,"column":13},"end":{"row":28,"column":28},"action":"remove","lines":["'smtp.zoho.com'"],"id":296},{"start":{"row":28,"column":13},"end":{"row":28,"column":25},"action":"insert","lines":["smtp.zoho.eu"]}],[{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["\""],"id":297}],[{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["\""],"id":298}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"remove","lines":["#"],"id":299},{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"remove","lines":["#"]},{"start":{"row":29,"column":28},"end":{"row":29,"column":29},"action":"remove","lines":["#"]},{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"remove","lines":["#"]},{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"remove","lines":["#"]},{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"remove","lines":["#"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"remove","lines":["#"]},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"remove","lines":["#"]},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"remove","lines":["#"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"remove","lines":["#"]},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"remove","lines":["#"]},{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"remove","lines":["#"]}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["l"],"id":300},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["i"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["a"]},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["m"]},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["b"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["r"]},{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["w"]},{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"insert","lines":["o"]},{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"insert","lines":["e"]},{"start":{"row":29,"column":28},"end":{"row":29,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":29,"column":28},"end":{"row":29,"column":29},"action":"remove","lines":["n"],"id":301},{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"remove","lines":["e"]},{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"remove","lines":["o"]},{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"remove","lines":["w"]}],[{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["o"],"id":302},{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"insert","lines":["w"]},{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"insert","lines":["n"]},{"start":{"row":29,"column":28},"end":{"row":29,"column":29},"action":"insert","lines":["e"]},{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"insert","lines":["b"]},{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"insert","lines":["u"]},{"start":{"row":29,"column":31},"end":{"row":29,"column":32},"action":"insert","lines":["s"]},{"start":{"row":29,"column":32},"end":{"row":29,"column":33},"action":"insert","lines":["i"]},{"start":{"row":29,"column":33},"end":{"row":29,"column":34},"action":"insert","lines":["n"]},{"start":{"row":29,"column":34},"end":{"row":29,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":29,"column":35},"end":{"row":29,"column":36},"action":"insert","lines":["s"],"id":303},{"start":{"row":29,"column":36},"end":{"row":29,"column":37},"action":"insert","lines":["s"]},{"start":{"row":29,"column":37},"end":{"row":29,"column":38},"action":"insert","lines":["."]},{"start":{"row":29,"column":38},"end":{"row":29,"column":39},"action":"insert","lines":["c"]},{"start":{"row":29,"column":39},"end":{"row":29,"column":40},"action":"insert","lines":["o"]}],[{"start":{"row":29,"column":39},"end":{"row":29,"column":40},"action":"remove","lines":["o"],"id":304},{"start":{"row":29,"column":38},"end":{"row":29,"column":39},"action":"remove","lines":["c"]},{"start":{"row":29,"column":37},"end":{"row":29,"column":38},"action":"remove","lines":["."]}],[{"start":{"row":29,"column":37},"end":{"row":29,"column":38},"action":"insert","lines":["@"],"id":305},{"start":{"row":29,"column":38},"end":{"row":29,"column":39},"action":"insert","lines":["g"]},{"start":{"row":29,"column":39},"end":{"row":29,"column":40},"action":"insert","lines":["m"]},{"start":{"row":29,"column":40},"end":{"row":29,"column":41},"action":"insert","lines":["a"]},{"start":{"row":29,"column":41},"end":{"row":29,"column":42},"action":"insert","lines":["i"]},{"start":{"row":29,"column":42},"end":{"row":29,"column":43},"action":"insert","lines":["l"]},{"start":{"row":29,"column":43},"end":{"row":29,"column":44},"action":"insert","lines":["."]},{"start":{"row":29,"column":44},"end":{"row":29,"column":45},"action":"insert","lines":["c"]},{"start":{"row":29,"column":45},"end":{"row":29,"column":46},"action":"insert","lines":["o"]},{"start":{"row":29,"column":46},"end":{"row":29,"column":47},"action":"insert","lines":["m"]}],[{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"remove","lines":["'"],"id":306},{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["#"]},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["#"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"remove","lines":["#"]},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"remove","lines":["#"]},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"remove","lines":["#"]},{"start":{"row":30,"column":27},"end":{"row":30,"column":28},"action":"remove","lines":["#"]},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"remove","lines":["#"]},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"remove","lines":["#"]},{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"remove","lines":["#"]},{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"remove","lines":["#"]},{"start":{"row":30,"column":22},"end":{"row":30,"column":23},"action":"remove","lines":["'"]}],[{"start":{"row":30,"column":22},"end":{"row":30,"column":50},"action":"insert","lines":["os.environ.get(\"SECRET_KEY\")"],"id":307}],[{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"remove","lines":["Y"],"id":308},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"remove","lines":["E"]},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"remove","lines":["K"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"remove","lines":["_"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":["T"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":["E"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":["R"]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["C"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["E"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"remove","lines":["S"]}],[{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"insert","lines":["E"],"id":309},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"insert","lines":["m"]}],[{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["m"],"id":310}],[{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"remove","lines":["E"],"id":311},{"start":{"row":30,"column":38},"end":{"row":30,"column":50},"action":"insert","lines":["EmailBackend"]}],[{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"remove","lines":["d"],"id":312},{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"remove","lines":["n"]},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"remove","lines":["e"]},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"remove","lines":["k"]},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"remove","lines":["c"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"remove","lines":["a"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":["B"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":["l"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":["i"]}],[{"start":{"row":30,"column":41},"end":{"row":30,"column":44},"action":"insert","lines":["   "],"id":313}],[{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":[" "],"id":314},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":[" "]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":[" "]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["a"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["m"]}],[{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"insert","lines":["M"],"id":315},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"insert","lines":["A"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":["I"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":["L"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"insert","lines":["_"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"insert","lines":["H"]},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"insert","lines":["O"]}],[{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"insert","lines":["S"],"id":316},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"insert","lines":["T"]}],[{"start":{"row":30,"column":38},"end":{"row":30,"column":48},"action":"remove","lines":["EMAIL_HOST"],"id":317},{"start":{"row":30,"column":38},"end":{"row":30,"column":57},"action":"insert","lines":["EMAIL_HOST_PASSWORD"]}],[{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":318},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["i"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["m"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["p"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["o"]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["r"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":[" "],"id":319},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["e"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["n"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":[" "],"id":320}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":11},"action":"remove","lines":["import env "],"id":321}],[{"start":{"row":29,"column":0},"end":{"row":34,"column":61},"action":"remove","lines":["EMAIL_HOST = \"smtp.zoho.eu\"","EMAIL_HOST_USER = 'liambrownebusiness@gmail.com'","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_HOST_PASSWORD\")","EMAIL_PORT = 587","EMAIL_USE_TLS = True","EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'"],"id":322}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["i"],"id":323},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["m"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["p"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["o"]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["r"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":[" "],"id":324},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["e"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["n"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":10},"action":"remove","lines":["import env"],"id":325},{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":326}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["i"],"id":328},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["m"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["p"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["o"]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["r"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":[" "],"id":329},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["e"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["n"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":[" "],"id":330}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["import env ",""],"id":331},{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":332},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["i"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["m"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["p"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["o"]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["r"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":[" "],"id":333},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["e"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["n"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":10},"action":"remove","lines":["import env"],"id":334},{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":115.5,"scrollleft":0,"selection":{"start":{"row":10,"column":22},"end":{"row":10,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1578345183543}