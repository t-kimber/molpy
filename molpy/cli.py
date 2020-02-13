import argparse
from .util import read_xyz, distance

def main():
	parser = argparse.ArgumentParser(description='A Molecule utility that reads XYZ files and calculates the distance between atoms at index1 and index2.')
	parser.add_argument('filename', type=str, help='The XYZ file to read.')
	parser.add_argument('index1', type=int, help='Index of the first atom.')
	parser.add_argument('index2', type=int, help='Index of the second atom.')

	args = parser.parse_args()

	print(args)
	print("-------------")
	mol = read_xyz(args.filename)

	distance_value = distance(mol["geometry"][args.index1,:], mol["geometry"][args.index2,:])

	print(f'Distance {distance_value}')