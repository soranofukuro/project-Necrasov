with open('bd.txt','r') as f2:
    bd=f2.read()
bd=bd.split(',')
def pon(k):
    for i in range(len(bd)):
        if bd[i] == k:
            return f"{bd[i - 1]},{bd[i]},{bd[i + 1]},{bd[i + 2]},{bd[i + 3]},{bd[i + 4]}"
for i in range(1,(118*6)-1,6):
    print(f"    def {bd[i]}_def(self):")
    print(f"        with open('bd.txt', 'r') as f2:")
    print(f"            bd = f2.read().split(',')")
    print(f"        self.label.setText(self.pon('{bd[i]}', bd))")
    print(f"        print(self.{bd[i]}.text())")
    print('')