DATABASE_DATA = [
    {
        "id": 1,
        "name": "Pendul triplu",
        "src": "images/pendulGravTriplu.gif",
        "info": "Simularea unui pendul triplu gravitational fara frecari.",
        "language": "Matlab"
    },
    {
        "id": 2,
        "name": "Pendul dublu",
        "src": "images/pendulGravDublu.gif",
        "info": "Simularea unui pendul dublu gravitational fara frecari.",
        "language": "Matlab"
    },
    {
        "id": 3,
        "name": "Oscilator armonic",
        "src": "images/oscilatorArmonic.gif",
        "info": "Simularea unui oscilator armonic.",
        "language": "Matlab"
    }
]

DEFAULT_POST = [
    {
        "id": 0,
        "name": "Default",
        "src": "images/default.jpg",
        "info": "-",
        "language": "-"
    }
]

ROW_LENGHT = 2 

def getRows():
    rows = []
    # if are lenght of datebase is odd. make it even
    if(len(DATABASE_DATA) % 2 != 0):
        DATABASE_DATA.extend(DEFAULT_POST)

    # make the rows
    row = []
    for data in DATABASE_DATA:
        row.append(data)
        if(len(row) == ROW_LENGHT):
          rows.append(row.copy())
          row.clear()
    return rows
"""
CREATE TABLE IF NOT EXISTS `mydb`.`Content` (
  `idContent` INT NOT NULL,
  `source` VARCHAR(150) NOT NULL,
  `name` VARCHAR(100) NULL,
  `informations` TEXT NULL,
  `language` TEXT NULL,
  `author` TEXT NULL,
  PRIMARY KEY (`idContent`),
  UNIQUE INDEX `idContent_UNIQUE` (`idContent` ASC))
ENGINE = InnoDB
"""
    