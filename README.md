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


#### 2. Meng-upload file proyek (lokal repositori) ke remote repositori (Github)

        # Meng-upload file
        # Langkah 1
        (aftar66) λ git status
        On branch main
        Your branch is ahead of 'origin/main' by 4 commits.
          (use "git push" to publish your local commits)

        nothing to commit, working tree clean

        # Langkah 2
        (aftar66) λ git push


#### 3. Menjalankan server kali pertama dan melaihat tampilan laman default Django di browser

        # Menjalankan development server (lokal server)
        (aftar66) λ

        (aftar66) λ ls
        config/  README.md  venv312503/

        (aftar66) λ cd config\

        (aftar66) λ ls
        config/  manage.py*

        (aftar66) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        April 27, 2024 - 22:39:06
        Django version 5.0.3, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


#### 4. Merubah struktur folder proyek

        modified:   README.md
        renamed:    config/config/__init__.py -> config/__init__.py
        renamed:    config/config/asgi.py -> config/asgi.py
        renamed:    config/config/settings.py -> config/settings.py
        renamed:    config/config/urls.py -> config/urls.py
        renamed:    config/config/wsgi.py -> config/wsgi.py
        renamed:    config/manage.py -> manage.py