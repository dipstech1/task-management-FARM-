
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field
class Settings(BaseSettings):
    MONGO_URI: str = Field(title = "MongoDB URI", default="")
    DB_NAME : str =  Field(title = "Databasename", default="")
    JWT_SECRET: str = Field(title="jwt secrect", default="")
    JWT_ALGORITHM: str = Field(title="jwt algo", default="")
    REDIS_URL: str = Field(title="redis url", default="")
    LOG_LEVEL: str = Field(title="Log level", default="INFO")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(title="Token expiration time", default=30)

    # Use model_config to specify a .env file to load from
    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()