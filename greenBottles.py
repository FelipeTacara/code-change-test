def greenbottles(bottles):
    for garrafas in range(bottles, 0, -1):
        # for loop counting down the number of bottles
        print(f"{garrafas} green bottles, hanging on the wall\n"
              f"{garrafas} green bottles, hanging on the wall\n"
              f"And if 1 green bottle should accidentally fall,\n"
              f"They'd be {garrafas - 1} green bottles hanging on the wall."
              f"...\n")
