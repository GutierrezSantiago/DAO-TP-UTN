from boundaries.PantallasLibros.PantallaLibros import PantallaLibros
from boundaries.PantallasLibros.PantallaCamposLibro import PantallaCamposLibro
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError
from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.BDHelper import BDHelper
from persistence.dtos.LibroDTO import LibroDTO
from entities.Libro import Libro

class LibrosController:
  def __init__(self, backToMain, dao: ILibroDAO = LibroDAOImplSQL()) -> None:
    self.pantalla = PantallaLibros(self, backToMain)
    BDHelper().suscribir(self.pantalla)
    self.dao = dao
    self.loadLibros()
    
  def loadLibros(self):
    self.libros = self.dao.fetchAll()
    self.pantalla.setLibros([(l.getCodigo(),)+l.asTuple() for l in self.libros])
    
  def search(self, id: int):
    if id == -1: 
      self.loadLibros()
      return
    try: libro = self.dao.fetchById(id)
    except RegistroNoEncontradoError:
      self.pantalla.setLibros([])
      return
    self.pantalla.setLibros([(libro.getCodigo(),) + libro.asTuple()])
    
  def desuscribir(self, observer): BDHelper().desuscribir(observer)
  
  def desbloquearPantalla(self): 
    self.pantalla.desbloquear()
    self.idLibro = None
  def bloquearPantalla(self): self.pantalla.bloquear()
  
  def volver(self):
    self.desuscribir(self.pantalla)
    self.pantalla.destruir()
    self.pantalla.volver()
  
  def create(self, libroDTO: LibroDTO): 
    libro = libroDTO.asLibro()
    self.dao.create(libro)
  
  def update(self, libroDTO: LibroDTO):
    libro = libroDTO.asLibro()
    libro._codigo = self.idLibro
    self.dao.update(libro)
    self.idLibro = None
    
  def delete(self):
    l = self.dao.fetchById(self.idLibro)
    if l.estaPrestado():
      self.pantalla.showErrorMessage("No se puede eliminar un libro que está prestado")
      return
    self.dao.delete(self.idLibro)
    self.idLibro = None
    
  def openCreateWindow(self):
    self.bloquearPantalla()
    PantallaCamposLibro(self, None, "C")
    
  def openReadWindow(self, data: tuple):
    self.bloquearPantalla()
    PantallaCamposLibro(self, data[1:], "R")
  
  def openUpdateWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idLibro = data[0]
    PantallaCamposLibro(self, data[1:], "U")
    
  def openDeleteWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idLibro = data[0]
    PantallaCamposLibro(self, data[1:], "D")