LINES=$(wc -l ${1} | cut -d' ' -f1)
SIZE=300
QRFOLDER="qrcodes"
BADGEFOLDER="crachas"

mkdir -p ${QRFOLDER}
mkdir -p ${BADGEFOLDER}

for i in $(seq 2 ${LINES})
do
	echo -ne "${i}/${LINES}\r"
	line=$(sed "${i}q;d" ${1})
	nome=$(echo ${line} | cut -d',' -f2 | sed "s/'//g")
	nome="${nome^^}"
	email=$(echo ${line} | cut -d',' -f3)
	id=$(echo ${line} | cut -d',' -f1)
	wget "http://chart.apis.google.com/chart?cht=qr&chs="${SIZE}"x"${SIZE}"&chl=${nome},${id},${email}" > /dev/null 2>&1 
	mv chart* "${QRFOLDER}/${nome}.png"
	convert ../cracha.png "${QRFOLDER}/${nome}.png" -geometry +94+94 -composite c.png
	convert c.png -stroke none -fill black -pointsize 46 -font "/home/${USER}/.fonts/RobotoCondensed-Regular.ttf" -annotate +125+590 "${nome}" "${BADGEFOLDER}/${nome}.png"
done

rm c.png 

