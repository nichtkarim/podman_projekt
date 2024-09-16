# Podman-Projekt mit SQLite und Flask API

Dieses Projekt demonstriert, wie man ein Podman-Projekt mit zwei rootless Containern auf Ubuntu erstellt.

## Projektstruktur:
- **SQLite-Container**: Eine einfache SQLite-Datenbank mit einem Benutzer `Karim`.
- **Flask API-Container**: Eine Flask API, die Daten aus der SQLite-Datenbank abruft.

### Schritte:

1. **Podman installieren** (falls nicht bereits installiert):
   ```bash
   sudo apt-get install podman
   ```

2. **Projektverzeichnis klonen und in das Verzeichnis wechseln**:
   ```bash
   git clone <dein-repo-link>
   cd podman_projekt
   ```

3. **SQLite-Container erstellen und starten**:
   ```bash
   podman build -t sqlite-container -f Dockerfile_sqlite .
   podman run -d --name sqlite_container sqlite-container
   ```

4. **API-Server-Container erstellen und starten**:
   ```bash
   podman build -t flask-api-container -f Dockerfile_flask .
   podman run -d -p 5000:5000 --name flask_api_container flask-api-container
   ```

5. **API testen**:
   ```bash
   curl http://localhost:5000/user
   ```
   Ausgabe:
   ```json
   {
       "name": "Karim"
   }
   ```
   