import os
from datetime import datetime
from pathlib import Path
from typing import IO

from frictionless import Package, Resource

from sprout.core.models import File
from sprout.core.utils import count_rows, get_datapackage_path, get_project_path


def load_project(project_name: str) -> "Package":
    """Load a frictionless.Package object from a datapackage.json metadata file.

    Args:
        project_name: name of the project folder
        
    Raises:
        FrictionlessException: if the specified datapackage.json file doesn't exist.

    Returns:
        Package: data package object for the project
    """
    return Package(get_datapackage_path(project_name))

def load_resource(project_name: str, resource_name: str) -> "Resource":
	project = load_project(project_name)
	return project.get_resource(resource_name)

def check_resource_exists_by_name(project_name: str, resource_name: str) -> bool:
	project = load_project(project_name)
	return project.has_resource(resource_name)

def link_file_to_resource(
		file: File, 
		resource: Resource, 
		file_row_count: int) -> "Resource":
	resource.custom["last_data_upload"] = datetime.now()
	resource.custom["files"].append(file)
	resource.custom["data_rows"] += file_row_count

	if resource.path is None:
		resource.path = file.path
	else:
		resource.extrapaths.append(file.path)

	return resource


def delete_file_from_resource(file_to_delete: File, resource: Resource):
	file_row_count = count_rows(file_to_delete.server_file_path)

	resource.custom["modified_at"] = datetime.now()
	resource.custom["files"] = [
		file for file in resource.custom["files"] 
		if file["path"] != file_to_delete.path
		]
	resource.custom["data_rows"] -= file_row_count

	if resource.path == file_to_delete.path:
		resource.path = resource.extrapaths[0] if resource.extrapaths else None
	else:
		resource.extrapaths = [
			path for path in resource.extrapaths 
			if path != file_to_delete.path
			]

	os.remove(file_to_delete.server_file_path)
	update_resource(resource)

def delete_all_files_from_resource(resource: Resource):
	file_paths = [file["server_file_path"] for file in resource.custom["files"]]
	for path in file_paths:
		os.remove(path)

	resource.custom["modified_at"] = datetime.now()
	resource.custom["files"] = []
	resource.custom["data_rows"] = 0
	resource.path = None
	resource.extrapaths = []

	update_resource(resource)

def save_project(project: Package):
	project.to_json(get_datapackage_path(project.name))

def update_resource(resource: Resource):
	resource.package.set_resource(resource)
	save_project(resource.package)

def upsert_resource(project: Package, resource: Resource):
	if project.has_resource(resource.name):
		update_resource(resource)
		return
	
	project.add_resource(resource)
	save_project(project)

def save_file(file: IO, output_file_name: str, project_name: str) -> str:
    """Upload and save a file into raw storage.

    Args:
        file: The file as an IO object
        output_file_name: The name of the file to store.
        project_name: The name of the project where the file belongs

    Returns:
        str: The path to the saved file.
    """
    output_path = Path(get_project_path(project_name), output_file_name)
    return write(file, output_path)

def write(file: IO, output_path: str) -> str:
    """Write a file to a specified path.

    Args:
        file: file to write
        output_path: path to write the file to

    Returns:
        str: The path to the written/saved file.
    """
    # Begin reading of file at the start of it
    file.seek(0)
    with open(output_path, "wb") as target:
        target.write(file.read())
    return output_path
