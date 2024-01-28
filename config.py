from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    debug: bool
    secret_key: str
    allowed_client_hosts: str
    email_host: str
    email_port: str
    email_host_user: str
    email_host_password: str
    email_use_tls: bool
    email_use_ssl: bool
    db_conn_max_age: int

    class Config:
        env_file = '.env'


settings = Settings()