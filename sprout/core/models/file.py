import os
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import IO, Optional, Type

from sprout.core.repository import save_file


@dataclass
class File:
	path: Path
	original_file_name: str
	server_file_path: Path
	file_extension: str
	file_size_bytes: int
	created_at: datetime
	created_by: Optional[int]
	modified_at: datetime

	@classmethod
	def from_file_io(cls: Type["File"], file: IO, project_name: str) -> "File":
		file_extension = file.name.split(".")[-1]
		file_name_wo_ext = file.name.split(".")[-2][:150]
		unique_file_name = f"{file_name_wo_ext}-{uuid.uuid4().hex}.{file_extension}"

		# TODO: first save data file to `raw`, validate it based on metadata, 
		# then move it to project folder?
		server_file_path = save_file(file, unique_file_name, project_name)

		return cls(
			path=unique_file_name, 
			original_file_name=file.name, 
			server_file_path=server_file_path, 
			file_extension=file_extension, 
			file_size_bytes=os.path.getsize(server_file_path),
			created_at=datetime.now(),
			created_by=None,
			modified_at=datetime.now()
			)
