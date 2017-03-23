
from BdioComponent import BdioComponent
from BdioExternalIdentifier import BdioExternalIdentifier
from BdioProject import BdioProject
from BdioRelationship import BdioRelationship
from BillOfMaterials import BillOfMaterials
from hub_python_plugin.BlackDuckPackage import BlackDuckPackage
from hub_python_plugin.BlackDuckSerializer import *


class Bdio(object):

    tree = None
    code_location_name = None

    def __init__(self, tree, code_location_name):
        self.tree = tree
        self.code_location_name = code_location_name
        if self.code_location_name is None:
            self.code_location_name = tree.name + "/" + tree.version

    def generate_bdio(self):
        bdio = []
        bom = self._get_bom()
        project = self._get_node(BdioProject(), self.tree)
        components = self._get_components()

        bdio.append(bom)
        bdio.append(project)
        bdio.extend(components)
        return bdio

    def _get_bom(self):
        bom = BillOfMaterials()
        bom.name = self.code_location_name + " Black Duck I/O Export"
        bom = map_from_object(bom)
        return bom

    def _get_node(self, node , package):
        node.id_ = package.get_internal_id()
        node.name = package.name
        node.version = package.version
        node.relationships = self._get_relationships(package)
        node.external_id = map_from_object(package.get_external_id())
        node = map_from_object(node)
        return node

    def _get_components(self):
        components = self.tree.flatten()
        components = [self._get_node(BdioComponent(), pkg) for pkg in components]
        return components

    def _get_relationships(self, package):
        relationships = []
        for pkg in package.dependencies:
            relationship = BdioRelationship()
            relationship.related = pkg.get_internal_id()
            relationship = map_from_object(relationship)
            relationships.append(relationship)
        return relationships