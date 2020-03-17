import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from pomop.models import ConceptClass, Cohort

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

engine = create_engine(f'postgresql://{os.getenv("USER")}:{os.getenv("PASS")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("DB_NAME")}')
Session = sessionmaker(bind=engine)

def main():
    logger.debug('boop')
    session = Session()
    result = session.query(Cohort).limit(10)
    for row in result:
        logger.debug(row)
        logger.debug(row.definition)

if __name__ == '__main__':
    main()