class Settings(BaseSettings):
    # ... (previous settings)
    
    POSTGRES_REPLICA_SERVERS: List[str] = []
    
    @validator("POSTGRES_REPLICA_SERVERS", pre=True)
    def split_replica_servers(cls, v: Optional[str]) -> List[str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

settings = Settings()

