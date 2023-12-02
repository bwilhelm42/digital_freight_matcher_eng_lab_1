import pandas as pd
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from models import Base, Route, Client, Location

# Database connection
DATABASE_URL = "mysql+pymysql://user:password123@db/dfm_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def load_data():
    session = Session()

    # Read data from Excel
    file_path = '/app/db/data/data_tables.xlsx'  # Adjust path if necessary
    dfs = pd.read_excel(file_path, sheet_name=None)

    # Load 'Client' data if not already present
    existing_client_ids = [c.id for c in session.query(Client.id).all()]
    for _, row in dfs['clients'].iterrows():
        if row['id'] not in existing_client_ids:
            client = Client(**row.to_dict())
            session.add(client)
    session.commit()

    # Load 'Location' data if not already present
    existing_location_ids = [l.id for l in session.query(Location.id).all()]
    for _, row in dfs['locations'].iterrows():
        if row['id'] not in existing_location_ids:
            location = Location(**row.to_dict())
            session.add(location)
    session.commit()

    # Load 'Route' data if not already present
    existing_route_ids = [r.id for r in session.query(Route.id).all()]
    for _, row in dfs['routes'].iterrows():
        if row['id'] not in existing_route_ids:
            route = Route(**row.to_dict())
            session.add(route)
    session.commit()

    session.close()

    print("INITIAL DATA LOAD COMPLETE")


if __name__ == "__main__":
    load_data()
