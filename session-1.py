

# for  i in range(1,11): # [intiail, end[
    # print(f"{i} x 5 == {i * 5}")

# # i = 1; i < 21; i = i + 1
# for  i in range(0, 21, 1):
#     # if i % 2 ==0:
#         print(i)


# factorial  n =  n * n-1 * n-2 * ... * 1
# n = int (input())

# fact = 1
# for i in range(n, 0, -1): # [n, 1[   == [n, 2]
#     fact = fact * i

# print(fact)



# for n; test if it is a prime number.

# prime number => Only divisable by n and 1.
# n = int(input())
# counter = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         print(f"{n} % {i} == {n % i}")
#         counter = counter + 1

#     if counter > 2:
#         break

# if counter == 2:
#     print("prime")
# else:
#     print("Not prime")

# student1 = input()
# student2 = input()
# student3 = input()
# student4 = input()
# student5 = input()


students = []

# students.append("messi")
# students.append(10)
# students.append(10.0)
# students.append(True)
# print(students)

# students.pop()
# print(students)
# students.remove("messi")
# print(students)
# students.insert(1, "messi")
# print(students)

# students = []
# for i in range(5):
#     students.append(input())

# for i in students:
#     print(i)


# Create a list the has the even numbers under 20.

# append(), remove(), pop(), insert()

x = []
for i in range(20):
    if i %2 == 0:
        x.append(i)

print(x)
