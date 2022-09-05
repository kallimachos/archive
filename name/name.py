#!/usr/bin/python3
"""Tavi name generator."""

# first = "Tavi"
# middle = [
#     ("William", "W", "W."),
#     ("William Moss", "WM", "W.M."),
#     ("William Geles", "WG", "W.G."),
#     # "Geles", "Moss",
# ]
# last = [
#     ("Moss", "M", "M."),
#     ("Geles", "G", "G."),
#     ("Moss Geles", "MG", "M.G."),
#     ("Moss-Geles", "M-G", "M.-G."),
#     ("Geles Moss", "GM", "G.M."),
#     ("Geles-Moss", "G-M", "G.-M."),
# ]

# print()
# for mid in middle:
#     for las in last:
#         if mid[0] in las[0] or (len(mid[0].split()) == 2 and mid[0].split()[1] in las[0]):
#             continue
#         print(
#             f"{first} {mid[0]} {las[0]:<15}"
#             f"{first} {las[0]:<12}"
#             f"{first} {las[1]:<7}"
#             f"{first[0]}.{mid[2]}{las[2]:<7}"
#             f"{first[0]}.{mid[2]}{las[1]:<7}"
#             f"{first[0]}{mid[1]}{las[1]:<7}"
#             f"{first[0]}.{las[2]:<7}"
#             f"{first[0]}{las[1]}"
#         )
# print()

print()

print("Tavi William Geles          Tavi Geles        Tavi G      T.W.G.      T.W.G      TWG      T.G.      TG\n"
      "Tavi William Geles-Moss     Tavi Geles-Moss   Tavi G-M    T.W.G.-M.   T.W.G-M    TWG-M    T.G.-M.   TG-M\n"
      "Tavi William Moss Geles     Tavi Geles        Tavi G      T.W.M.G.    T.W.M.G    TWMG     T.G.      TG\n"
      "Tavi William Geles Moss     Tavi Moss         Tavi M      T.W.G.M.    T.W.G.M    TWGM     T.M.      TM")
print()
