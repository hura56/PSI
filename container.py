from dependency_injector import containers, providers


from services.weather_service import WeatherService
import os
import subprocess
if os.getenv('a') == '1':
    from repositories.weather_repo_db import WeatherRepo
elif os.getenv('a') == '0':
    from repositories.weather_repo_txt import WeatherRepo
class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepo,
    )

    service = providers.Factory(
        WeatherService,
        repo=repo,
    )
