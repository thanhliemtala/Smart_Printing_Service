from run import app,db, Printer

printer_list = [["TOSHIBA","E-studio 656","CS1.H1"],
                ["TOSHIBA","E-studio 656","CS1.H1"],
                ["TOSHIBA","E-studio 656","CS1.H2"],
                ["TOSHIBA","E-studio 656","CS1.H2"],
                ["TOSHIBA","E-studio 656","CS1.H3"],
                ["TOSHIBA","E-studio 656","CS1.H3"],
                ["TOSHIBA","E-studio 656","CS1.H6"],
                ["TOSHIBA","E-studio 656","CS1.H6"],
                ["TOSHIBA","E-studio 656","CS1.A4"],
                ["TOSHIBA","E-studio 656","CS1.A5"],
                ["TOSHIBA","E-studio 656","CS1.A5"],
                ["TOSHIBA","E-studio 656","CS1.B1"],
                ["TOSHIBA","E-studio 656","CS1.B5"],
                ["TOSHIBA","E-studio 656","CS1.C4"],
                ["TOSHIBA","E-studio 656","CS1.C5"],
                ]

def add_Printer(printer_list):
    for printer in printer_list:
        new_printer = Printer(brand_name=printer[0],is_on=True, location=printer[2],notes="None",print_model=printer[1]) 
        with app.app_context():
            db.session.add(new_printer) 
            db.session.commit()
            
add_Printer(printer_list)

# Query all:
with app.app_context():
    printer = Printer.query.all()
    print(printer)