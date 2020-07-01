if [ -z "${1}" ]
then
	echo "usage: ${0} file.csv"
	exit
fi

path='../'
file=$path$1

cd scripts

chmod +x gerador_crachas.sh

./gerador_crachas.sh ${file}

mv ./crachas ../

mv ./qrcodes ../

