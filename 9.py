import sqlite3
import webbrowser
import folium
from sqlite3 import Error
from os import system, name


def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def create_db_table():
    conn = None
    try:
        conn = sqlite3.connect('sqlite.db')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.execute(
                """create table if not exists contacts (
                        id integer primary key autoincrement,
                        DNI integer unique,
                        first_name text,
                        last_name text,
                        phone integer,
                        latitude real,
                        longitude real
                    )
                """
            )
            conn.close()

def list_db_data():
    conn = None
    try:
        conn = sqlite3.connect('sqlite.db')
    except Error as e:
        print(e)
    finally:
        if conn:
            data_list = []
            cur = conn.cursor()
            cur.execute('SELECT * FROM contacts')
            rows = cur.fetchall()
            
            for i in rows:
                data_list.append(dict(zip([c[0] for c in cur.description], i)))

            conn.close()
            return data_list

def retrieve_db_data(DNI):
    conn = None
    try:
        conn = sqlite3.connect('sqlite.db')
    except Error as e:
        print(e)
    finally:
        if conn:
            cur = conn.cursor()
            cur.execute(
               f'SELECT * FROM contacts WHERE DNI={DNI}'
            )
            
            rows = cur.fetchall()
            conn.close()
            if rows:
                return dict(zip([c[0] for c in cur.description], rows[0]))
            else:
                return None

def insert_db_data(data):
    conn = None
    try:
        conn = sqlite3.connect('sqlite.db')
    except Error as e:
        print(e)
    finally:
        if conn:
            try:
                conn.execute(
                    """
                    insert into contacts(
                    DNI,
                    first_name, 
                    last_name, 
                    phone, 
                    latitude, 
                    longitude) 
                    values (?,?,?,?,?,?)
                    """
                    
                    , data
                )
                conn.commit()
                conn.close()
                return {'err': False, 'message': 'Contacto agregado.'}
            except sqlite3.IntegrityError:
                conn.close()
                return {'err': True, 'message': 'Ya existe un contacto con el mismo DNI.'}

def update_db_data(data):
    conn = None
    try:
        conn = sqlite3.connect('sqlite.db')
    except Error as e:
        print(e)
    finally:
        if conn:
            try:
                conn.execute(
                f"""
                    UPDATE contacts
                    SET DNI = ?,
                    first_name = ?, 
                    last_name = ?,
                    phone = ?, 
                    latitude = ?, 
                    longitude = ?
                    WHERE id = {data[0]}
                """
                , (data[1], data[2], data[3], data[4], data[5], data[6])
                )
                conn.commit()
                conn.close()
                return {'err': False, 'message': 'Contacto modificado.'}
            except Error as e:
                return {'err': True, 'message': 'Hubo un error al modificar el contacto.', 'e': e}

def delete_db_data(DNI):
    conn = None
    try:
        conn = sqlite3.connect('sqlite.db')
    except Error as e:
        print(e)
    finally:
        if conn:
            try:
                contact = retrieve_db_data(DNI)
                if contact:
                    conn.execute(
                    f'DELETE FROM contacts WHERE DNI={contact.get("DNI")}'
                    )
                    conn.commit()
                    conn.close()
                    return {'err': False, 'message': 'Contacto eliminado.'}
                conn.close()
                return {'err': True, 'message': 'Contacto no encontrado.'}
            except:
                conn.close()
                return {'err': True, 'message': 'Hubo un error al eliminar el contacto.'}

def list_data():
    clear_console()
    print(
        """
                    Contactos
        Ingrese 0 en el campo volver atrás.
        """
    )

    while True:
        try:
            print(
                    f"""
______________________________________________________________
| DNI        | Nombre        | Apellido      | Celular       |
--------------------------------------------------------------"""
                )
            for i in list_db_data():
                print(
                    f"""
{i.get('DNI')}        {i.get('first_name')}       {i.get('last_name')}        {i.get('phone')}
"""
                )
            value = int(input('Ingrese 0 para volver atrás: '))
        except:
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break

def retrieve_data():
    clear_console()
    print(
        """
                                    Buscar contacto
        Ingrese el DNI del contacto que quieres buscar o ingrese 0 para volver atrás.
        """
    )

    while True:
        try:
            value = int(input('Ingrese un valor: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break
            elif len(str(value)) == 8 or len(str(value)) == 7:
                data = retrieve_db_data(value)
                if data:
                    print(
                        f"""
______________________________________________________________
| DNI        | Nombre        | Apellido      | Celular       |
--------------------------------------------------------------
{data.get('DNI')}        {data.get('first_name')}       {data.get('last_name')}        {data.get('phone')}
                        """
                    )
                else:
                    print(
                f"""
        No se encontró ningún contacto con el DNI {value}.
                    Vuelve a intentarlo.
                """)

def add_data():
    clear_console()
    print(
        """
                    Agregar contacto
        Ingrese 0 en el campo DNI para volver atrás.
        
        """
    )
    while True:
        try:
            dni = int(input('Ingrese el DNI: '))
            if dni == 0:
                break
            first_name = input('Ingrese el nombre: ')
            last_name = input('Ingrese el apellido: ')
            phone = int(input('Ingrese el celular: '))
            latitude = float(input('Ingrese la latitud: '))
            longitude = float(input('Ingrese la longitud: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if dni and first_name and last_name and phone and latitude and longitude:
                if first_name.isalpha() and last_name.isalpha():
                    create = insert_db_data((dni, first_name, last_name, phone, latitude, longitude))
                    if create['err']:
                        clear_console()
                        print(
                            f"""
        {create['message']}
                            """
                        )
                    else:
                        clear_console()
                        print(create['message'])
                        break

def update_data():
    clear_console()

    while True:
        print(
            """
                                        Modificar contacto
            Ingrese el DNI del contacto que quieres modifigar o ingrese 0 para volver atrás.
            """
        )
        try:
            value = int(input('Ingrese el DNI: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break
            elif len(str(value)) == 8 or len(str(value)) == 7:
                previous = retrieve_db_data(value)
                if previous:
                    clear_console()
                    print(
                        f"""
                    Contacto a modificar
        Ingrese 0 en el campo DNI para volver atrás.
______________________________________________________________
| DNI        | Nombre        | Apellido      | Celular       |
--------------------------------------------------------------
{previous.get('DNI')}        {previous.get('first_name')}       {previous.get('last_name')}        {previous.get('phone')}
                        """
                    )
                    while True:
                        try:
                            dni = int(input('Ingrese el nuevo DNI: '))
                            if dni == 0:
                                break
                            first_name = input('Ingrese el nuevo nombre: ')
                            last_name = input('Ingrese el nuevo apellido: ')
                            phone = int(input('Ingrese el nuevo celular: '))
                            latitude = float(input('Ingrese la nueva latitud: '))
                            longitude = float(input('Ingrese la nueva longitud: '))
                        except:
                            clear_console()
                            print(
                                """
                        Error, el tipo de dato ingresado no es corecto.
                                    Vuelve a intentarlo.
                                """)
                        else:
                            if dni and first_name and last_name and phone and latitude and longitude:
                                if first_name.isalpha() and last_name.isalpha():
                                    update = update_db_data((previous.get('id'), dni, first_name, last_name, phone, latitude, longitude))
                                    if update['err']:
                                        clear_console()
                                        print(
                                            f"""
                        {update['message']}
                                            """
                                        )
                                    else:
                                        clear_console()
                                        print(update['message'])
                                        break
                else:
                    clear_console()
                    print(
                        f"""
                No se encontró ningún contacto con el DNI {value}.
                            Vuelve a intentarlo.
                        """) 
            

            else:
                print(
                """
        El DNI ingresado es incorrecto.
            Vuelve a intentarlo.
                """)

def delete_data():
    clear_console()
    print(
        """
                                    Eliminar contacto
        Ingrese el DNI del contacto que quieres eliminar o ingrese 0 para volver atrás.
        """
    )

    while True:
        try:
            value = int(input('Ingrese el DNI: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break
            elif len(str(value)) == 8 or len(str(value)) == 7:
                data = delete_db_data(value)
                if data['err']:
                    print(
                        f"""
    {data['message']}
                        """
                    )
                else:
                    print(
                        f"""
    {data['message']}
                        """
                    )
            else:
                print(
                """
        El DNI ingresado es incorrecto.
            Vuelve a intentarlo.
                """)

def get_contact_on_map():
    clear_console()
    print(
        """
                                    Ver contacto en el mapa
        Ingrese el DNI del contacto al que quieres ver en el mapa o ingrese 0 para volver atrás.
        """
    )

    while True:
        try:
            value = int(input('Ingrese el DNI: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break
            elif len(str(value)) == 8 or len(str(value)) == 7:
                data = retrieve_db_data(value)
                if data:
                    m = folium.Map(location=[data.get('latitude'), data.get('longitude')], zoom_start=11)
                    folium.Marker(
                        [data.get('latitude'), data.get('longitude')], popup=f"{data.get('first_name')} {data.get('last_name')} {data.get('phone')}", tooltip='Abrir'
                    ).add_to(m)
                    m.save('map.html')
                    webbrowser.open_new('map.html')
                    break
                else:
                    print(
                f"""
        No se encontró ningún contacto con el DNI {value}.
                    Vuelve a intentarlo.
        #         """)

def get_all_contacts_on_map():
    clear_console()
    print(
        """
                             Ver contactos en el mapa
        """
    )

    while True:

        data = list_db_data()
        if data:
            m = folium.Map(location=[-26.783333333333, -60.45], zoom_start=11)
            for i in data:
                folium.Marker(
                    [i.get('latitude'), i.get('longitude')], popup=f"{i.get('first_name')} {i.get('last_name')} {i.get('phone')}", tooltip=f"{i.get('first_name')} {i.get('last_name')} {i.get('phone')}"
                ).add_to(m)
            
            m.save('map.html')
            webbrowser.open_new('map.html')
            break

        try:
            value = int(input('\nIngrese 0 para volver atrás: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break
            else:
                print(
                f"""
        Debe ingresar el número 0 para volver atrás.
                    Vuelve a intentarlo.
                """)

def send_wa_contact():
    clear_console()
    print(
        """
                                    Enviar WhatsApp a un contacto
        Ingrese el DNI del contacto al que quieres enviar un WhatsApp o ingrese 0 para volver atrás.
        """
    )

    while True:
        try:
            value = int(input('Ingrese el DNI: '))
        except:
            clear_console()
            print(
                """
        Error, el tipo de dato ingresado no es corecto.
                    Vuelve a intentarlo.
                """)
        else:
            if value == 0:
                break
            elif len(str(value)) == 8 or len(str(value)) == 7:
                data = retrieve_db_data(value)
                if data:
                    webbrowser.open_new(f'https://wa.me/54{data.get("phone")}?text=Hola')
                    break
                else:
                    print(
                f"""
        No se encontró ningún contacto con el DNI {value}.
                    Vuelve a intentarlo.
                """)

while True:
    clear_console()

    print(
        """
              ¡Bienvenido!
        Por favor elige una opción.

1) Listar contactos.
2) Buscar un contacto.
3) Insertar un contacto.
4) Modificar un contacto.
5) Eliminar un contacto.
6) Ver un contacto en el mapa.
7) Ver todos los contactos en el mapa.
8) Enviar WhatsApp a un contacto.
0) Salir.
        """
    )

    try:
        value = int(input('Ingrese un valor numérico: '))
    except:
        print('Deve ingresar una opción numérica.')
    else:
        if value == 0:
            break
        elif value == 1:
            list_data()
        elif value == 2:
            retrieve_data()
        elif value == 3:
            add_data()
        elif value == 4:
            update_data()
        elif value == 5:
            delete_data()
        elif value == 6:
            get_contact_on_map()
        elif value == 7:
            get_all_contacts_on_map()
        elif value == 8:
            send_wa_contact()