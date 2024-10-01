#!/usr/bin/env python3
def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http","https"]
    print(proto)
    proto.append("dns")
    protoa.append("dns")
    print(proto)
    proto2 = [22, 80, 443, 53]
    proto.extend(proto2) 
    print(proto)
    protoa.append(proto2)
    print(protoa)
    index_of_element = proto2.index(proto2[3])
    print(f"The index of element 53 in proto2 is: {index_of_element}")
main()
