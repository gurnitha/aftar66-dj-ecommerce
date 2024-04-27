# aftar66-dj-ecommerce
Membuat aplikasi ecommerce menggunakan Django versi 5.0.3, memperingati tgl. lahir saya yang ke-66.


## 1. SETUP

#### 1. Membuat repositori baru di Github
#### 2. Mengklon repositori baru dari Github
#### 3. Membuat lingkungan virtual dengan nama venv312503
#### 4. Mengkatifkan venv312503
#### 5. Menginstal Django versi 5.0.3

        modified:   .gitignore
        modified:   README.md


## 2. MEMBUAT PROYEK DAN APLIKASI DJANGO


#### 1. Membuat proyek dengan nama config

        # Memeriksa perintah untuk membuat proyek
        (aftar66) λ django-admin
            ...
            dbshell
            makemigrations
            migrate
            runserver
            shell
            sqlmigrate
            startapp
            startproject
            ...

        # Membuat proyek
        (aftar66) λ django-admin startproject config

        # Struktur folder proyek
        config
        │   manage.py
        │
        └───config
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py

        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py

        # Menyimpan file pada lokal repositori di komputer
        # Langkah 1
        (aftar66) λ git add .

        # Langkah 2
        (aftar66) λ git status
        On branch main
        Your branch is ahead of 'origin/main' by 2 commits.
          (use "git push" to publish your local commits)

        Changes to be committed:
          (use "git restore --staged <file>..." to unstage)
                modified:   README.md
                new file:   config/config/__init__.py
                new file:   config/config/asgi.py
                new file:   config/config/settings.py
                new file:   config/config/urls.py
                new file:   config/config/wsgi.py
                new file:   config/manage.py


        # Langkah 3
        (aftar66) λ git commit -am "1. Membuat proyek dengan nama config"
        [main 6a25796] 1. Membuat proyek dengan nama config
         7 files changed, 236 insertions(+)
         create mode 100644 config/config/__init__.py
         create mode 100644 config/config/asgi.py
         create mode 100644 config/config/settings.py
         create mode 100644 config/config/urls.py
         create mode 100644 config/config/wsgi.py
         create mode 100644 config/manage.py