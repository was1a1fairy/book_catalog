import moduls
import ui

path = ui.message("введите название каталога", str)
path = moduls.check_path(path)

def main():
  while True:
    ui.core(path)


if __name__ == "__main__":
  main()



