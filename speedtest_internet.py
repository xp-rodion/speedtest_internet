import speedtest

sp = speedtest.Speedtest(secure=True)

def script_information() -> None:
    print('''
            It's simple internet speedtest.
            This script can output your ping, download/upload speed.
            Inspection -->
            To choose what to measure the speed of the internet:
                B - Speed in bytes;
                KB - Speed in KB;
                MB - Speed in MB;
    ''')


def calculate_by_speed(num):
    num.upper()
    speed_dd = speed_ud = 0
    sp.get_best_server()
    ping = sp.results.ping
    if num in ['B', 'KB', 'MB']:
        print('Wait, the data is being computed...')
        match num:
            case 'B':
                speed_dd = sp.download()
                speed_ud = sp.upload()
            case 'KB':
                speed_dd = sp.download() / pow(2, 10)
                speed_ud = sp.upload() / pow(2, 10)
            case 'MB':
                speed_dd = sp.download() / pow(2, 20)
                speed_ud = sp.upload() / pow(2, 20)
        return (speed_dd, speed_ud, ping, num)
    else:
        return "Error"


def return_speed_information(calc_info) -> None:
        if type(calc_info) == tuple:
            print('Computed Internet Values: ')
            print(f'Downloads speed --> {calc_info[0]} {calc_info[3]}/s')
            print(f'Uploads speed--> {calc_info[1]} {calc_info[3]}/s')
            print(f'Your ping --> {calc_info[2]} ms')
        else:
            print("Please, check your data option")

            

def main():
    script_information()
    return_speed_information(calculate_by_speed(input('Enter the option: ')))


if __name__ == '__main__':
    main()