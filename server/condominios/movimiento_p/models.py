from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence,Time
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ..vehiculo.models import *
from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property
