from math import prod

LITERAL_VALUE_OP = 4
TOTAL_LENGTH_ID = 0
TOTAL_LENGTH_BITS = 15
NUMBER_PACKETS_BITS = 11


def read_packet(binary, version_total=0):
    sub_packets = []
    version = int(binary[:3], 2)
    operator = int(binary[3:6], 2)
    version_total += version

    if operator == LITERAL_VALUE_OP:
        remaining, sub_packets = read_literal(binary[6:])
    else:
        length_type = int(binary[6])

        if length_type == TOTAL_LENGTH_ID:
            size = int(binary[7:7+TOTAL_LENGTH_BITS], 2)
            continue_reading = True
            to_read = binary[7+TOTAL_LENGTH_BITS:7+TOTAL_LENGTH_BITS+size]
            while continue_reading:
                to_read, version_total, sub = read_packet(to_read, version_total)
                sub_packets.append(sub)
                continue_reading = bool(int(to_read)) if len(to_read) > 0 else False
            remaining = binary[7+TOTAL_LENGTH_BITS+size:]
        else:
            packets = int(binary[7:7+NUMBER_PACKETS_BITS], 2)
            remaining = binary[7+NUMBER_PACKETS_BITS:]
            for _ in range(packets):
                remaining, version_total, sub = read_packet(remaining, version_total)
                sub_packets.append(sub)

        sub_packets = do_operation(operator, sub_packets)

    return remaining, version_total, sub_packets


def read_literal(string):
    pos = 0
    read_more = True
    number = ""
    while read_more:
        read_more = bool(int(string[pos]))
        number += string[pos+1:pos+5]
        pos += 5

    return string[pos:], int(number, 2)


def do_operation(operator, sub_packets):
    if operator == 0:
        sub_packets = sum(sub_packets)
    elif operator == 1:
        sub_packets = prod(sub_packets)
    elif operator == 2:
        sub_packets = min(sub_packets)
    elif operator == 3:
        sub_packets = max(sub_packets)
    elif operator == 5:
        sub_packets = int(sub_packets[0] > sub_packets[1])
    elif operator == 6:
        sub_packets = int(sub_packets[0] < sub_packets[1])
    elif operator == 7:
        sub_packets = int(sub_packets[0] == sub_packets[1])
    return sub_packets


def evaluate_bits(hex_number):
    binary = bin(int(hex_number, 16))[2:].zfill(len(hex_number)*4)
    _, version_total, sub_packets = read_packet(binary)
    print("Version total: ", version_total)
    print("Value: ", sub_packets)


if __name__ == '__main__':
    hex = "E20D79005573F71DA0054E48527EF97D3004653BB1FC006867A8B1371AC49C801039171941340066E6B99A6A58B8110088BA008CE6F7893D4E6F7893DCDCFDB9D6CBC4026FE8026200DC7D84B1C00010A89507E3CCEE37B592014D3C01491B6697A83CB4F59E5E7FFA5CC66D4BC6F05D3004E6BB742B004E7E6B3375A46CF91D8C027911797589E17920F4009BE72DA8D2E4523DCEE86A8018C4AD3C7F2D2D02C5B9FF53366E3004658DB0012A963891D168801D08480485B005C0010A883116308002171AA24C679E0394EB898023331E60AB401294D98CA6CD8C01D9B349E0A99363003E655D40289CBDBB2F55D25E53ECAF14D9ABBB4CC726F038C011B0044401987D0BE0C00021B04E2546499DE824C015B004A7755B570013F2DD8627C65C02186F2996E9CCD04E5718C5CBCC016B004A4F61B27B0D9B8633F9344D57B0C1D3805537ADFA21F231C6EC9F3D3089FF7CD25E5941200C96801F191C77091238EE13A704A7CCC802B3B00567F192296259ABD9C400282915B9F6E98879823046C0010C626C966A19351EE27DE86C8E6968F2BE3D2008EE540FC01196989CD9410055725480D60025737BA1547D700727B9A89B444971830070401F8D70BA3B8803F16A3FC2D00043621C3B8A733C8BD880212BCDEE9D34929164D5CB08032594E5E1D25C0055E5B771E966783240220CD19E802E200F4588450BC401A8FB14E0A1805B36F3243B2833247536B70BDC00A60348880C7730039400B402A91009F650028C00E2020918077610021C00C1002D80512601188803B4000C148025010036727EE5AD6B445CC011E00B825E14F4BBF5F97853D2EFD6256F8FFE9F3B001420C01A88915E259002191EE2F4392004323E44A8B4C0069CEF34D304C001AB94379D149BD904507004A6D466B618402477802E200D47383719C0010F8A507A294CC9C90024A967C9995EE2933BA840"
    evaluate_bits(hex)
