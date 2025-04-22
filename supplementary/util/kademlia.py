import pandas as pd


class KademliaNetwork:
    def __init__(self, node_ids, bits):
        self.node_ids = sorted(node_ids)
        self.m = bits
        self.max_id = 2**bits
        self.node_binaries = {node: format(node, f"0{self.m}b") for node in node_ids}

    def common_prefix_length(self, a_bin, b_bin):
        length = 0
        for a, b in zip(a_bin, b_bin):
            if a != b:
                break
            length += 1
        return length

    def xor_distance(self, a, b):
        return a ^ b

    def analyze_node(self, input_node_id):
        input_bin = format(input_node_id, f"0{self.m}b")
        prefix_groups = {i: [] for i in range(self.m)}

        for node, node_bin in self.node_binaries.items():
            if node == input_node_id:
                continue
            prefix_len = self.common_prefix_length(input_bin, node_bin)
            xor_dist = self.xor_distance(input_node_id, node)
            prefix_groups[prefix_len].append((node, node_bin, xor_dist))

        return input_bin, prefix_groups

    def display_all_nodes(self):
        print("\n=== Network Nodes ===")
        print(f"Using {self.m}-bit identifiers")
        print("Node ID | Binary Address")
        print("-" * 25)
        for node_id in self.node_ids:
            print(f"{node_id:7d} | {self.node_binaries[node_id]}")
        print("-" * 25)

    def get_routing_table(self, input_node_id):
        input_bin, result = self.analyze_node(input_node_id)
        routing_table = {}

        for prefix_len, entries in result.items():
            if entries:
                closest_node = min(entries, key=lambda x: x[2])
                routing_table[prefix_len] = closest_node

        return routing_table

    def display_analysis(self, input_node_id):
        input_bin, result = self.analyze_node(input_node_id)

        rows = []
        for prefix_len, entries in result.items():
            for node_id, node_bin, xor_dist in entries:
                rows.append(
                    {
                        "Node ID": node_id,
                        "Binary": node_bin,
                        "Prefix Length": prefix_len,
                        "XOR Distance": xor_dist,
                    }
                )

        if rows:
            print(f"\n=== Analysis for Node {input_node_id} ({input_bin}) ===")
            print("\n[All Nodes Analysis]")
            df = pd.DataFrame(rows).sort_values(
                by=["Prefix Length", "XOR Distance"], ascending=[True, True]
            )
            print(df.to_string(index=False))

            routing_table = self.get_routing_table(input_node_id)
            print("\n[Routing Table]")
            print("Prefix Length | Node ID | Binary | XOR Distance")
            print("-" * 50)

            for prefix_len in range(self.m):
                if prefix_len in routing_table:
                    node_id, node_bin, xor_dist = routing_table[prefix_len]
                    print(f"{prefix_len:12d} | {node_id:7d} | {node_bin} | {xor_dist}")
                else:
                    print(f"{prefix_len:12d} | {'empty':>7s} | {'':6s} | {'':3s}")
            print("-" * 50)
        else:
            print("\nNo other nodes to analyze.")


def get_valid_nodes():
    while True:
        try:
            nodes_input = input("Enter node IDs (space-separated numbers): ")
            nodes = [int(x) for x in nodes_input.split()]
            if not nodes:
                print("Please enter at least one node ID")
                continue
            return nodes
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces")


def get_valid_bits():
    while True:
        try:
            bits = int(input("Enter number of identifier bits (m): "))
            if bits <= 0:
                print("Number of bits must be positive")
                continue
            return bits
        except ValueError:
            print("Invalid input. Please enter a positive number")


def main():
    print("\n=== Kademlia Network Setup ===")
    nodes = get_valid_nodes()
    bits = get_valid_bits()

    network = KademliaNetwork(nodes, bits)

    network.display_all_nodes()

    while True:
        try:
            print("\nEnter a node ID to analyze (non-number to exit)")
            input_node_id = int(input(">>> "))

            if input_node_id >= network.max_id:
                print(
                    f"Warning: Node ID must be less than {network.max_id} for {bits}-bit identifiers"
                )
                continue

            if input_node_id not in network.node_ids:
                print(f"Warning: Node {input_node_id} is not in the network")

            network.display_analysis(input_node_id)

        except ValueError:
            print("\nExiting program...")
            break


if __name__ == "__main__":
    main()
