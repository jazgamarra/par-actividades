
# API de Sistema de Facturación y Stock

Base URL: http://localhost:8080/par2024

Esta API permite gestionar facturas, productos, clientes y proveedores, con operaciones completas CRUD (Crear, Leer, Actualizar, Eliminar). Está pensada para integrarse en sistemas de facturación, inventario y control de ventas.

## Endpoints

### Facturas
GET /facturas
Obtiene la lista de todas las facturas.

`POST /facturas`
Crea una nueva factura.

`GET /facturas/{id}`
Obtiene una factura específica por su ID.

`PUT /facturas/{id}`
Actualiza los datos de una factura existente.

`DELETE /facturas/{id}`
Elimina una factura por su ID.

### Productos

`GET /productos`
Lista todos los productos en stock.

`POST /productos`
Crea un nuevo producto.

`GET /productos/{id}`
Obtiene un producto por su ID.

`PUT /productos/{id}`
Actualiza los datos de un producto existente.

`DELETE /productos/{id}`
Elimina un producto por su ID.

### Clientes

`GET /clientes`
Lista todos los clientes registrados.

`POST /clientes`
Crea un nuevo cliente.

`GET /clientes/{id}`
Obtiene un cliente por su ID.

`PUT /clientes/{id}`
Actualiza los datos de un cliente existente.

`DELETE /clientes/{id}`
Elimina un cliente por su ID.

### Proveedores
`GET /proveedores`
Lista todos los proveedores registrados.

`POST /proveedores`
Crea una nueva factura.

`GET /proveedores/{id}`
Obtiene un proveedor por su ID.

`PUT /proveedores/{id}`
Actualiza los datos de un proveedor existente.

`DELETE /proveedores/{id}`
Elimina un proveedor por su ID.

--- 
Jazmin Gamarra, 20/03/2025.