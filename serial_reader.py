# serial_reader.py
import serial, time, csv, sqlite3
from datetime import datetime

SERIAL_PORT = 'COM3'   # or '/dev/ttyUSB0'
BAUD = 115200
DB = 'energy.db'
CSV = 'realtime_energy.csv'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS readings (
                    id INTEGER PRIMARY KEY,
                    ts TEXT, voltage REAL, current REAL, power REAL)''')
    conn.commit()
    conn.close()

def run():
    init_db()
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=2)
    time.sleep(2)
    with open(CSV, 'a', newline='') as f:
        writer = csv.writer(f)
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        while True:
            line = ser.readline().decode('utf-8').strip()
            # expected: "voltage,current"
            if not line: 
                continue
            try:
                v, i = map(float, line.split(','))
            except:
                continue
            power = v * i
            ts = datetime.now().isoformat()
            writer.writerow([ts, v, i, power])
            conn.execute("INSERT INTO readings (ts, voltage, current, power) VALUES (?,?,?,?)",
                         (ts, v, i, power))
            conn.commit()
            print(ts, v, i, power)

if __name__ == '__main__':
    run()
