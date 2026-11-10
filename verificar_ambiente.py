
import sys

print("================================")
print("       ATLAS AI - SYSTEM")
print("================================")

print(f"Python: {sys.version}")
print(f"Executavel: {sys.executable}")

try:
    import fastapi
    import httpx
    import pydantic

    print("\nDependencias principais:")
    print("FastAPI: OK")
    print("HTTPX: OK")
    print("Pydantic: OK")

    print("\nAmbiente preparado com sucesso!")

except ImportError as erro:
    print(f"Erro ao importar dependencia: {erro}")
