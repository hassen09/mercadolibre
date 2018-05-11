import scrapy
import re
from mercadolibre.items import MercadolibreItem


class MercaSpider(scrapy.Spider):
    name = 'mercadoAvril'
    # allowed_domains = ['autos.mercadolibre.com.mx']
    # start_urls=[        'https://autos.mercadolibre.com.mx/'] #tous les annonce impossible ccar affichage de 15000 annonce ct
#commande de start url = response.xpath("//section[@class='modal-overlay modal-location-filter modal-location-filter-9991744-AMLM_1744_2']/div[@class='modal-container']/div[@class='modal-content']/div[@class='container']/div[@class='group']/div[@class='filters']/div/div/a/@href").extract()
#le site limite mon spider par max de 2000 announce par lien 
    start_urls = ['https://autos.mercadolibre.com.mx/dodge/1000/',
                 'https://autos.mercadolibre.com.mx/mclaren/12c-spider/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/147/',
                 'https://autos.mercadolibre.com.mx/chevrolet/1500/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/156/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/166/',
                 'https://autos.mercadolibre.com.mx/chrysler/200/',
                 'https://autos.mercadolibre.com.mx/peugeot/2008/',
                 'https://autos.mercadolibre.com.mx/peugeot/206/',
                 'https://autos.mercadolibre.com.mx/peugeot/207/',
                 'https://autos.mercadolibre.com.mx/peugeot/208/',
                 'https://autos.mercadolibre.com.mx/nissan/240sx/',
                 'https://autos.mercadolibre.com.mx/300/',
                 'https://autos.mercadolibre.com.mx/peugeot/3008/',
                 'https://autos.mercadolibre.com.mx/peugeot/301/',
                 'https://autos.mercadolibre.com.mx/peugeot/306/',
                 'https://autos.mercadolibre.com.mx/peugeot/307/',
                 'https://autos.mercadolibre.com.mx/peugeot/308/',
                 'https://autos.mercadolibre.com.mx/chevrolet/3500/',
                 'https://autos.mercadolibre.com.mx/nissan/350z/',
                 'https://autos.mercadolibre.com.mx/ferrari/360/',
                 'https://autos.mercadolibre.com.mx/nissan/370z/',
                 'https://autos.mercadolibre.com.mx/ra/4000/',
                 'https://autos.mercadolibre.com.mx/peugeot/406/',
                 'https://autos.mercadolibre.com.mx/peugeot/407/',
                 'https://autos.mercadolibre.com.mx/ferrari/430/',
                 'https://autos.mercadolibre.com.mx/ferrari/458/',
                 'https://autos.mercadolibre.com.mx/ferrari/456/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/4c/',
                 'https://autos.mercadolibre.com.mx/toyota/4runner/',
                 'https://autos.mercadolibre.com.mx/fiat/500/',
                 'https://autos.mercadolibre.com.mx/peugeot/508/',
                 'https://autos.mercadolibre.com.mx/ferrari/550/',
                 'https://autos.mercadolibre.com.mx/mclaren/570gt/',
                 'https://autos.mercadolibre.com.mx/ferrari/599/',
                 'https://autos.mercadolibre.com.mx/peugeot/607/',
                 'https://autos.mercadolibre.com.mx/mclaren/650s-coupe/',
                 'https://autos.mercadolibre.com.mx/mclaren/650s-spider/',
                 'https://autos.mercadolibre.com.mx/mclaren/675lt-coupe/',
                 'https://autos.mercadolibre.com.mx/ra/700/',
                 'https://autos.mercadolibre.com.mx/porsche/718/',
                 'https://autos.mercadolibre.com.mx/mclaren/720-s-coupe/',
                 'https://autos.mercadolibre.com.mx/rover/75/',
                 'https://autos.mercadolibre.com.mx/saab/9-3/',
                 'https://autos.mercadolibre.com.mx/saab/9-5/',
                 'https://autos.mercadolibre.com.mx/porsche/911/',
                 'https://autos.mercadolibre.com.mx/audi/a1/',
                 'https://autos.mercadolibre.com.mx/audi/a3/',
                 'https://autos.mercadolibre.com.mx/audi/a4/',
                 'https://autos.mercadolibre.com.mx/audi/a5/',
                 'https://autos.mercadolibre.com.mx/audi/a6/',
                 'https://autos.mercadolibre.com.mx/audi/a7/',
                 'https://autos.mercadolibre.com.mx/audi/a8/',
                 'https://autos.mercadolibre.com.mx/audi/a9/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/asx/',
                 'https://autos.mercadolibre.com.mx/cadillac/ats/',
                 'https://autos.mercadolibre.com.mx/cadillac/ats-coupe/',
                 'https://autos.mercadolibre.com.mx/gmc/acadia/',
                 'https://autos.mercadolibre.com.mx/hyundai/accent/',
                 'https://autos.mercadolibre.com.mx/honda/accord/',
                 'https://autos.mercadolibre.com.mx/suzuki/aerio/',
                 'https://autos.mercadolibre.com.mx/ford/aerostar-/',
                 'https://autos.mercadolibre.com.mx/fiat/albea/',
                 'https://autos.mercadolibre.com.mx/seat/alhambra/',
                 'https://autos.mercadolibre.com.mx/nissan/almera/',
                 'https://autos.mercadolibre.com.mx/seat/altea/',
                 'https://autos.mercadolibre.com.mx/nissan/altima/',
                 'https://autos.mercadolibre.com.mx/volkswagen/amarok/',
                 'https://autos.mercadolibre.com.mx/isuzu/amigo/',
                 'https://autos.mercadolibre.com.mx/nissan/aprio/',
                 'https://autos.mercadolibre.com.mx/nissan/armada/',
                 'https://autos.mercadolibre.com.mx/chrysler/aspen/',
                 'https://autos.mercadolibre.com.mx/astra/',
                 'https://autos.mercadolibre.com.mx/chevrolet/astro/',
                 'https://autos.mercadolibre.com.mx/gmc/astrovan/',
                 'https://autos.mercadolibre.com.mx/seat/ateca/',
                 'https://autos.mercadolibre.com.mx/atos/',
                 'https://autos.mercadolibre.com.mx/dodge/attitude/',
                 'https://autos.mercadolibre.com.mx/satur/aura/',
                 'https://autos.mercadolibre.com.mx/chevrolet/avalanche/',
                 'https://autos.mercadolibre.com.mx/toyota/avalon/',
                 'https://autos.mercadolibre.com.mx/toyota/avanza/',
                 'https://autos.mercadolibre.com.mx/dodge/avenger/',
                 'https://autos.mercadolibre.com.mx/lamborghini/aventador/',
                 'https://autos.mercadolibre.com.mx/chevrolet/aveo/',
                 'https://autos.mercadolibre.com.mx/lincoln/aviator/',
                 'https://autos.mercadolibre.com.mx/pontiac/aztek/',
                 'https://autos.mercadolibre.com.mx/baic/bj40/',
                 'https://autos.mercadolibre.com.mx/cadillac/bls/',
                 'https://autos.mercadolibre.com.mx/subaru/brz/',
                 'https://autos.mercadolibre.com.mx/chevrolet/beat/',
                 'https://autos.mercadolibre.com.mx/volkswagen/beetle/',
                 'https://autos.mercadolibre.com.mx/chevrolet/beretta/',
                 'https://autos.mercadolibre.com.mx/lincoln/blackwood/',
                 'https://autos.mercadolibre.com.mx/chevrolet/blazer/',
                 'https://autos.mercadolibre.com.mx/seat/bocanegra/',
                 'https://autos.mercadolibre.com.mx/pontiac/bonneville/',
                 'https://autos.mercadolibre.com.mx/volkswagen/bora/',
                 'https://autos.mercadolibre.com.mx/volkswagen/bora-sportwagen/',
                 'https://autos.mercadolibre.com.mx/porsche/boxster/',
                 'https://autos.mercadolibre.com.mx/chrysler/breeze/',
                 'https://autos.mercadolibre.com.mx/ford/bronco/',
                 'https://autos.mercadolibre.com.mx/chevrolet/buick-/',
                 'https://autos.mercadolibre.com.mx/chevrolet/c-15/',
                 'https://autos.mercadolibre.com.mx/chevrolet/c-20/',
                 'https://autos.mercadolibre.com.mx/chevrolet/c-35/',
                 'https://autos.mercadolibre.com.mx/volvo/c30/',
                 'https://autos.mercadolibre.com.mx/volvo/c70/',
                 'https://autos.mercadolibre.com.mx/volkswagen/cc/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clk/',
                 'https://autos.mercadolibre.com.mx/honda/cr-v/',
                 'https://autos.mercadolibre.com.mx/honda/cr-z/',
                 'https://autos.mercadolibre.com.mx/cadillac/cts/',
                 'https://autos.mercadolibre.com.mx/mazda/cx-3/',
                 'https://autos.mercadolibre.com.mx/mazda/cx-5/',
                 'https://autos.mercadolibre.com.mx/mazda/cx-7/',
                 'https://autos.mercadolibre.com.mx/mazda/cx-9/',
                 'https://autos.mercadolibre.com.mx/nissan/cabstar/',
                 'https://autos.mercadolibre.com.mx/volkswagen/caddy/',
                 'https://autos.mercadolibre.com.mx/dodge/caliber/',
                 'https://autos.mercadolibre.com.mx/ferrari/california/',
                 'https://autos.mercadolibre.com.mx/chevrolet/camaro/',
                 'https://autos.mercadolibre.com.mx/chevrolet/camaro-zli/',
                 'https://autos.mercadolibre.com.mx/camry/',
                 'https://autos.mercadolibre.com.mx/gmc/canyon/',
                 'https://autos.mercadolibre.com.mx/chevrolet/caprice/',
                 'https://autos.mercadolibre.com.mx/chevrolet/captiva/',
                 'https://autos.mercadolibre.com.mx/renault/captur/',
                 'https://autos.mercadolibre.com.mx/caravan/',
                 'https://autos.mercadolibre.com.mx/porsche/carrera/',
                 'https://autos.mercadolibre.com.mx/cadillac/catera/',
                 'https://autos.mercadolibre.com.mx/chevrolet/cavalier/',
                 'https://autos.mercadolibre.com.mx/chevrolet/cavalier-z24/',
                 'https://autos.mercadolibre.com.mx/porsche/cayenne/',
                 'https://autos.mercadolibre.com.mx/porsche/cayman/',
                 'https://autos.mercadolibre.com.mx/toyota/celica/',
                 'https://autos.mercadolibre.com.mx/chevrolet/century/',
                 'https://autos.mercadolibre.com.mx/dodge/challenger/',
                 'https://autos.mercadolibre.com.mx/dodge/charger/',
                 'https://autos.mercadolibre.com.mx/jeep/cherokee/',
                 'https://autos.mercadolibre.com.mx/chevrolet/chevy/',
                 'https://autos.mercadolibre.com.mx/chevrolet/chevy-nova/',
                 'https://autos.mercadolibre.com.mx/chevrolet/chevy-pick-up/',
                 'https://autos.mercadolibre.com.mx/chevrolet/chevy-van/',
                 'https://autos.mercadolibre.com.mx/chevrolet/cheyenne/',
                 'https://autos.mercadolibre.com.mx/suzuki/ciaz/',
                 'https://autos.mercadolibre.com.mx/chrysler/cirrus/',
                 'https://autos.mercadolibre.com.mx/honda/city/',
                 'https://autos.mercadolibre.com.mx/honda/civic/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-a/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-b/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-c/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-cl/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-cla/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-cls/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-e/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-g/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-gl/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-gla/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-glc/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-gle/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-glk/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-gls/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-m/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-r/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-s/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-sl/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-slc/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/clase-slk/',
                 'https://autos.mercadolibre.com.mx/renault/clio/',
                 'https://autos.mercadolibre.com.mx/ford/club-wagon/',
                 'https://autos.mercadolibre.com.mx/mini/clubman/',
                 'https://autos.mercadolibre.com.mx/chevrolet/colorado/',
                 'https://autos.mercadolibre.com.mx/volkswagen/combi/',
                 'https://autos.mercadolibre.com.mx/jeep/commander/',
                 'https://autos.mercadolibre.com.mx/jeep/compass/',
                 'https://autos.mercadolibre.com.mx/chrysler/concorde/',
                 'https://autos.mercadolibre.com.mx/continental/',
                 'https://autos.mercadolibre.com.mx/ford/contour/',
                 'https://autos.mercadolibre.com.mx/mini/cooper-s/',
                 'https://autos.mercadolibre.com.mx/toyota/corolla/',
                 'https://autos.mercadolibre.com.mx/toyota/corona/',
                 'https://autos.mercadolibre.com.mx/corsa/',
                 'https://autos.mercadolibre.com.mx/chevrolet/corvette/',
                 'https://autos.mercadolibre.com.mx/ford/cougar/',
                 'https://autos.mercadolibre.com.mx/mini/countryman/',
                 'https://autos.mercadolibre.com.mx/ford/courier/',
                 'https://autos.mercadolibre.com.mx/volkswagen/crafter/',
                 'https://autos.mercadolibre.com.mx/kia/credos/',
                 'https://autos.mercadolibre.com.mx/hyundai/creta/',
                 'https://autos.mercadolibre.com.mx/volkswagen/crossgolf/',
                 'https://autos.mercadolibre.com.mx/chrysler/crossfire/',
                 'https://autos.mercadolibre.com.mx/volkswagen/crossfox/',
                 'https://autos.mercadolibre.com.mx/honda/crosstour/',
                 'https://autos.mercadolibre.com.mx/ford/crown-victoria/',
                 'https://autos.mercadolibre.com.mx/chevrolet/cruze/',
                 'https://autos.mercadolibre.com.mx/chevrolet/cutlass/',
                 'https://autos.mercadolibre.com.mx/seat/cordoba/',
                 'https://autos.mercadolibre.com.mx/dodge/d-100/',
                 'https://autos.mercadolibre.com.mx/dodge/d-150/',
                 'https://autos.mercadolibre.com.mx/dodge/d-250/',
                 'https://autos.mercadolibre.com.mx/dodge/d350/',
                 'https://autos.mercadolibre.com.mx/baic/d20/',
                 'https://autos.mercadolibre.com.mx/aston-martin/db11/',
                 'https://autos.mercadolibre.com.mx/aston-martin/db9/',
                 'https://autos.mercadolibre.com.mx/cadillac/dts/',
                 'https://autos.mercadolibre.com.mx/dodge/dakota/',
                 'https://autos.mercadolibre.com.mx/dart/',
                 'https://autos.mercadolibre.com.mx/land-rover/defender/',
                 'https://autos.mercadolibre.com.mx/volkswagen/derby/',
                 'https://autos.mercadolibre.com.mx/cadillac/deville/',
                 'https://autos.mercadolibre.com.mx/land-rover/discovery/',
                 'https://autos.mercadolibre.com.mx/land-rover/discovery-sport/',
                 'https://autos.mercadolibre.com.mx/nissan/doble-cabina/',
                 'https://autos.mercadolibre.com.mx/fiat/ducato/',
                 'https://autos.mercadolibre.com.mx/dodge/durango/',
                 'https://autos.mercadolibre.com.mx/renault/duster/',
                 'https://autos.mercadolibre.com.mx/ford/e-150/',
                 'https://autos.mercadolibre.com.mx/ford/e-350/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/eclipse/',
                 'https://autos.mercadolibre.com.mx/ford/ecosport/',
                 'https://autos.mercadolibre.com.mx/ford/econoline/',
                 'https://autos.mercadolibre.com.mx/ford/edge/',
                 'https://autos.mercadolibre.com.mx/cadillac/el-dorado/',
                 'https://autos.mercadolibre.com.mx/hyundai/elantra/',
                 'https://autos.mercadolibre.com.mx/honda/element/',
                 'https://autos.mercadolibre.com.mx/lotus/elise/',
                 'https://autos.mercadolibre.com.mx/buick/enclave/',
                 'https://autos.mercadolibre.com.mx/buick/encore/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/endeavor/',
                 'https://autos.mercadolibre.com.mx/buick/envision/',
                 'https://autos.mercadolibre.com.mx/volkswagen/eos/',
                 'https://autos.mercadolibre.com.mx/chevrolet/epica/',
                 'https://autos.mercadolibre.com.mx/chevrolet/equinox/',
                 'https://autos.mercadolibre.com.mx/cadillac/escalade/',
                 'https://autos.mercadolibre.com.mx/cadillac/escalade-esv/',
                 'https://autos.mercadolibre.com.mx/cadillac/escalade-ext/',
                 'https://autos.mercadolibre.com.mx/ford/escape/',
                 'https://autos.mercadolibre.com.mx/ford/escort/',
                 'https://autos.mercadolibre.com.mx/renault/euro-clio/',
                 'https://autos.mercadolibre.com.mx/volkswagen/eurovan/',
                 'https://autos.mercadolibre.com.mx/land-rover/evoque/',
                 'https://autos.mercadolibre.com.mx/lotus/evora-400/',
                 'https://autos.mercadolibre.com.mx/ford/excursion/',
                 'https://autos.mercadolibre.com.mx/seat/exeo/',
                 'https://autos.mercadolibre.com.mx/lotus/exige/',
                 'https://autos.mercadolibre.com.mx/ford/expedition/',
                 'https://autos.mercadolibre.com.mx/peugeot/expert/',
                 'https://autos.mercadolibre.com.mx/ford/explorer/',
                 'https://autos.mercadolibre.com.mx/ford/explorer-sport-trac/',
                 'https://autos.mercadolibre.com.mx/chevrolet/express/',
                 'https://autos.mercadolibre.com.mx/ford/f-150/',
                 'https://autos.mercadolibre.com.mx/ford/f-200/',
                 'https://autos.mercadolibre.com.mx/ford/f-250/',
                 'https://autos.mercadolibre.com.mx/ford/f-350/',
                 'https://autos.mercadolibre.com.mx/ford/f-450/',
                 'https://autos.mercadolibre.com.mx/ford/f-550/',
                 'https://autos.mercadolibre.com.mx/ford/f-600/',
                 'https://autos.mercadolibre.com.mx/jaguar/f-pace/',
                 'https://autos.mercadolibre.com.mx/jaguar/f-type/',
                 'https://autos.mercadolibre.com.mx/faw/f1/',
                 'https://autos.mercadolibre.com.mx/faw/f4/',
                 'https://autos.mercadolibre.com.mx/faw/f5/',
                 'https://autos.mercadolibre.com.mx/toyota/fj-cruiser/',
                 'https://autos.mercadolibre.com.mx/infiniti-/fx/',
                 'https://autos.mercadolibre.com.mx/ford/fairmont/',
                 'https://autos.mercadolibre.com.mx/ford/fiesta/',
                 'https://autos.mercadolibre.com.mx/ford/figo/',
                 'https://autos.mercadolibre.com.mx/pontiac/firebird/',
                 'https://autos.mercadolibre.com.mx/honda/fit/',
                 'https://autos.mercadolibre.com.mx/ford/five-hundred/',
                 'https://autos.mercadolibre.com.mx/cadillac/fleetwood/',
                 'https://autos.mercadolibre.com.mx/renault/fluence/',
                 'https://autos.mercadolibre.com.mx/bentley/flying-spur/',
                 'https://autos.mercadolibre.com.mx/ford/focus/',
                 'https://autos.mercadolibre.com.mx/ford/ford-gt/',
                 'https://autos.mercadolibre.com.mx/subaru/forester/',
                 'https://autos.mercadolibre.com.mx/smart-/forfour/',
                 'https://autos.mercadolibre.com.mx/kia/forte/',
                 'https://autos.mercadolibre.com.mx/smart-/fortwo/',
                 'https://autos.mercadolibre.com.mx/land-rover/freelander/',
                 'https://autos.mercadolibre.com.mx/ford/freestar/',
                 'https://autos.mercadolibre.com.mx/seat/freetrack/',
                 'https://autos.mercadolibre.com.mx/nissan/frontier/',
                 'https://autos.mercadolibre.com.mx/ford/fusion/',
                 'https://autos.mercadolibre.com.mx/pontiac/g3/',
                 'https://autos.mercadolibre.com.mx/infiniti-/g37/',
                 'https://autos.mercadolibre.com.mx/pontiac/g4/',
                 'https://autos.mercadolibre.com.mx/pontiac/g5/',
                 'https://autos.mercadolibre.com.mx/pontiac/g6/',
                 'https://autos.mercadolibre.com.mx/gt/',
                 'https://autos.mercadolibre.com.mx/nissan/gt-r/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/galant/',
                 'https://autos.mercadolibre.com.mx/lamborghini/gallardo/',
                 'https://autos.mercadolibre.com.mx/chevrolet/geo/',
                 'https://autos.mercadolibre.com.mx/ford/ghia/',
                 'https://autos.mercadolibre.com.mx/maserati/ghibli/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/giulia/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/giulietta/',
                 'https://autos.mercadolibre.com.mx/volkswagen/gol/',
                 'https://autos.mercadolibre.com.mx/volkswagen/golf/',
                 'https://autos.mercadolibre.com.mx/volkswagen/golf-gti/',
                 'https://autos.mercadolibre.com.mx/maserati/grancabrio/',
                 'https://autos.mercadolibre.com.mx/pontiac/grand-am/',
                 'https://autos.mercadolibre.com.mx/grand-caravan/',
                 'https://autos.mercadolibre.com.mx/jeep/grand-cherokee/',
                 'https://autos.mercadolibre.com.mx/ford/grand-marquis/',
                 'https://autos.mercadolibre.com.mx/pontiac/grand-prix/',
                 'https://autos.mercadolibre.com.mx/peugeot/grand-raid/',
                 'https://autos.mercadolibre.com.mx/suzuki/grand-vitara/',
                 'https://autos.mercadolibre.com.mx/hyundai/grand-i10/',
                 'https://autos.mercadolibre.com.mx/chrysler/grand-voyager/',
                 'https://autos.mercadolibre.com.mx/fiat/grande-punto/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/grandis/',
                 'https://autos.mercadolibre.com.mx/maserati/granturismo/',
                 'https://autos.mercadolibre.com.mx/h1/',
                 'https://autos.mercadolibre.com.mx/h100/',
                 'https://autos.mercadolibre.com.mx/hummer/h2/',
                 'https://autos.mercadolibre.com.mx/hummer/h3/',
                 'https://autos.mercadolibre.com.mx/chevrolet/hhr/',
                 'https://autos.mercadolibre.com.mx/honda/hr-v/',
                 'https://autos.mercadolibre.com.mx/ford/harley-davidson/',
                 'https://autos.mercadolibre.com.mx/toyota/hiace/',
                 'https://autos.mercadolibre.com.mx/toyota/highlander/',
                 'https://autos.mercadolibre.com.mx/nissan/hikari/',
                 'https://autos.mercadolibre.com.mx/toyota/hilux/',
                 'https://autos.mercadolibre.com.mx/lamborghini/huracan/',
                 'https://autos.mercadolibre.com.mx/i30/',
                 'https://autos.mercadolibre.com.mx/infiniti-/i35/',
                 'https://autos.mercadolibre.com.mx/acura/ilx/',
                 'https://autos.mercadolibre.com.mx/lexus/is/',
                 'https://autos.mercadolibre.com.mx/seat/ibiza/',
                 'https://autos.mercadolibre.com.mx/nissan/ichi-van/',
                 'https://autos.mercadolibre.com.mx/fiat/idea/',
                 'https://autos.mercadolibre.com.mx/fiat/idea-adventure/',
                 'https://autos.mercadolibre.com.mx/ford/ikon/',
                 'https://autos.mercadolibre.com.mx/chevrolet/impala/',
                 'https://autos.mercadolibre.com.mx/subaru/impreza/',
                 'https://autos.mercadolibre.com.mx/nissan/infiniti/',
                 'https://autos.mercadolibre.com.mx/dodge/intrepid/',
                 'https://autos.mercadolibre.com.mx/hyundai/ix35/',
                 'https://autos.mercadolibre.com.mx/i10/',
                 'https://autos.mercadolibre.com.mx/bmw/i3/',
                 'https://autos.mercadolibre.com.mx/bmw/i8/',
                 'https://autos.mercadolibre.com.mx/infiniti-/jx/',
                 'https://autos.mercadolibre.com.mx/infiniti-/jx35/',
                 'https://autos.mercadolibre.com.mx/volkswagen/jetta/',
                 'https://autos.mercadolibre.com.mx/volkswagen/jetta-clasico/',
                 'https://autos.mercadolibre.com.mx/gmc/jimmy/',
                 'https://autos.mercadolibre.com.mx/mini/john-cooper-works/',
                 'https://autos.mercadolibre.com.mx/dodge/journey/',
                 'https://autos.mercadolibre.com.mx/nissan/juke/',
                 'https://autos.mercadolibre.com.mx/ford/ka/',
                 'https://autos.mercadolibre.com.mx/renault/kangoo/',
                 'https://autos.mercadolibre.com.mx/nissan/kicks/',
                 'https://autos.mercadolibre.com.mx/nissan/king-cab/',
                 'https://autos.mercadolibre.com.mx/suzuki/kizashi/',
                 'https://autos.mercadolibre.com.mx/renault/koleos/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/l200/',
                 'https://autos.mercadolibre.com.mx/land-rover/lr2/',
                 'https://autos.mercadolibre.com.mx/land-rover/lr3/',
                 'https://autos.mercadolibre.com.mx/land-rover/lr4/',
                 'https://autos.mercadolibre.com.mx/ls/',
                 'https://autos.mercadolibre.com.mx/chevrolet/luv/',
                 'https://autos.mercadolibre.com.mx/buick/lacrosse/',
                 'https://autos.mercadolibre.com.mx/renault/laguna/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/lancer/',
                 'https://autos.mercadolibre.com.mx/toyota/land-cruiser/',
                 'https://autos.mercadolibre.com.mx/nissan/leaf/',
                 'https://autos.mercadolibre.com.mx/subaru/legacy/',
                 'https://autos.mercadolibre.com.mx/seat/leon/',
                 'https://autos.mercadolibre.com.mx/maserati/levante/',
                 'https://autos.mercadolibre.com.mx/jeep/liberty/',
                 'https://autos.mercadolibre.com.mx/fiat/linea/',
                 'https://autos.mercadolibre.com.mx/ford/lobo/',
                 'https://autos.mercadolibre.com.mx/ford/lobo-raptor-svt/',
                 'https://autos.mercadolibre.com.mx/renault/logan/',
                 'https://autos.mercadolibre.com.mx/nissan/lucino/',
                 'https://autos.mercadolibre.com.mx/chevrolet/lumina/',
                 'https://autos.mercadolibre.com.mx/volkswagen/lupo/',
                 'https://autos.mercadolibre.com.mx/infiniti-/m/',
                 'https://autos.mercadolibre.com.mx/acura/mdx/',
                 'https://autos.mercadolibre.com.mx/lincoln/mkc/',
                 'https://autos.mercadolibre.com.mx/lincoln/mks/',
                 'https://autos.mercadolibre.com.mx/lincoln/mkx/',
                 'https://autos.mercadolibre.com.mx/lincoln/mkz/',
                 'https://autos.mercadolibre.com.mx/toyota/mr2/',
                 'https://autos.mercadolibre.com.mx/mx-5/',
                 'https://autos.mercadolibre.com.mx/porsche/macan/',
                 'https://autos.mercadolibre.com.mx/chrysler/magnum/',
                 'https://autos.mercadolibre.com.mx/chevrolet/malibu/',
                 'https://autos.mercadolibre.com.mx/peugeot/manager/',
                 'https://autos.mercadolibre.com.mx/nissan/march/',
                 'https://autos.mercadolibre.com.mx/mercury/mariner/',
                 'https://autos.mercadolibre.com.mx/lincoln/mark-lt/',
                 'https://autos.mercadolibre.com.mx/lincoln/mark-viii/',
                 'https://autos.mercadolibre.com.mx/matiz/',
                 'https://autos.mercadolibre.com.mx/matrix/',
                 'https://autos.mercadolibre.com.mx/ford/maverick/',
                 'https://autos.mercadolibre.com.mx/nissan/maxima/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/maybac/',
                 'https://autos.mercadolibre.com.mx/mazda/mazda-2/',
                 'https://autos.mercadolibre.com.mx/mazda/mazda-3/',
                 'https://autos.mercadolibre.com.mx/mazda/5/',
                 'https://autos.mercadolibre.com.mx/mazda/mazda-6/',
                 'https://autos.mercadolibre.com.mx/mazda/mazda-speed-3/',
                 'https://autos.mercadolibre.com.mx/ford/mercury-/',
                 'https://autos.mercadolibre.com.mx/meriva/',
                 'https://autos.mercadolibre.com.mx/nissan/micra/',
                 'https://autos.mercadolibre.com.mx/mercury/milan/',
                 'https://autos.mercadolibre.com.mx/mini-cooper/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/mirage/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/mito/',
                 'https://autos.mercadolibre.com.mx/fiat/mobi/',
                 'https://autos.mercadolibre.com.mx/tesla/model-x/',
                 'https://autos.mercadolibre.com.mx/ford/mondeo/',
                 'https://autos.mercadolibre.com.mx/pontiac/montana/',
                 'https://autos.mercadolibre.com.mx/pontiac/montana-sv6/',
                 'https://autos.mercadolibre.com.mx/chevrolet/monte-carlo/',
                 'https://autos.mercadolibre.com.mx/montego/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/montero/',
                 'https://autos.mercadolibre.com.mx/mercury/mountaineer/',
                 'https://autos.mercadolibre.com.mx/nissan/murano/',
                 'https://autos.mercadolibre.com.mx/ford/mustang/',
                 'https://autos.mercadolibre.com.mx/mystique/',
                 'https://autos.mercadolibre.com.mx/renault/megane/',
                 'https://autos.mercadolibre.com.mx/nissan/np300/',
                 'https://autos.mercadolibre.com.mx/nissan/np300-frontier/',
                 'https://autos.mercadolibre.com.mx/acura/nsx/',
                 'https://autos.mercadolibre.com.mx/nissan/nv-2500/',
                 'https://autos.mercadolibre.com.mx/lincoln/navigator/',
                 'https://autos.mercadolibre.com.mx/neon/',
                 'https://autos.mercadolibre.com.mx/chrysler/new-yorker/',
                 'https://autos.mercadolibre.com.mx/kia/niro/',
                 'https://autos.mercadolibre.com.mx/dodge/nitro/',
                 'https://autos.mercadolibre.com.mx/nissan/note/',
                 'https://autos.mercadolibre.com.mx/honda/odyssey/',
                 'https://autos.mercadolibre.com.mx/chevrolet/oldsmobile-silhouette/',
                 'https://autos.mercadolibre.com.mx/kia/optima/',
                 'https://autos.mercadolibre.com.mx/chevrolet/optra/',
                 'https://autos.mercadolibre.com.mx/otros-modelos/',
                 'https://autos.mercadolibre.com.mx/subaru/outback/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/outlander/',
                 'https://autos.mercadolibre.com.mx/satur/outlook/',
                 'https://autos.mercadolibre.com.mx/chrysler/pt-cruiser/',
                 'https://autos.mercadolibre.com.mx/mini/paceman/',
                 'https://autos.mercadolibre.com.mx/chrysler/pacifica/',
                 'https://autos.mercadolibre.com.mx/fiat/palio/',
                 'https://autos.mercadolibre.com.mx/fiat/palio-adventure/',
                 'https://autos.mercadolibre.com.mx/porsche/panamera/',
                 'https://autos.mercadolibre.com.mx/fiat/panda/',
                 'https://autos.mercadolibre.com.mx/peugeot/partner/',
                 'https://autos.mercadolibre.com.mx/peugeot/partner-tepee/',
                 'https://autos.mercadolibre.com.mx/volkswagen/passat/',
                 'https://autos.mercadolibre.com.mx/honda/passport/',
                 'https://autos.mercadolibre.com.mx/nissan/pathfinder/',
                 'https://autos.mercadolibre.com.mx/jeep/patriot/',
                 'https://autos.mercadolibre.com.mx/phantom/',
                 'https://autos.mercadolibre.com.mx/pick-up/',
                 'https://autos.mercadolibre.com.mx/honda/pilot/',
                 'https://autos.mercadolibre.com.mx/nissan/platina/',
                 'https://autos.mercadolibre.com.mx/chrysler/plymount/',
                 'https://autos.mercadolibre.com.mx/volkswagen/pointer/',
                 'https://autos.mercadolibre.com.mx/volkswagen/pointer-pick-up/',
                 'https://autos.mercadolibre.com.mx/ford/police/',
                 'https://autos.mercadolibre.com.mx/volkswagen/polo/',
                 'https://autos.mercadolibre.com.mx/volkswagen/polo-gti/',
                 'https://autos.mercadolibre.com.mx/toyota/prius/',
                 'https://autos.mercadolibre.com.mx/ford/probe/',
                 'https://autos.mercadolibre.com.mx/ra/promaster/',
                 'https://autos.mercadolibre.com.mx/ra/promaster-rapid/',
                 'https://autos.mercadolibre.com.mx/fiat/punto/',
                 'https://autos.mercadolibre.com.mx/audi/q3/',
                 'https://autos.mercadolibre.com.mx/infiniti-/q45/',
                 'https://autos.mercadolibre.com.mx/audi/q5/',
                 'https://autos.mercadolibre.com.mx/infiniti-/q50/',
                 'https://autos.mercadolibre.com.mx/infiniti-/q60/',
                 'https://autos.mercadolibre.com.mx/audi/q7/',
                 'https://autos.mercadolibre.com.mx/infiniti-/q70/',
                 'https://autos.mercadolibre.com.mx/infiniti-/qx30/',
                 'https://autos.mercadolibre.com.mx/infiniti-/qx56/',
                 'https://autos.mercadolibre.com.mx/infiniti-/qx60/',
                 'https://autos.mercadolibre.com.mx/infiniti-/qx70/',
                 'https://autos.mercadolibre.com.mx/infiniti-/qx80/',
                 'https://autos.mercadolibre.com.mx/maserati/quattroporte/',
                 'https://autos.mercadolibre.com.mx/nissan/quest/',
                 'https://autos.mercadolibre.com.mx/audi/r8/',
                 'https://autos.mercadolibre.com.mx/toyota/rav4/',
                 'https://autos.mercadolibre.com.mx/peugeot/rcz/',
                 'https://autos.mercadolibre.com.mx/acura/rdx/',
                 'https://autos.mercadolibre.com.mx/acura/rl/',
                 'https://autos.mercadolibre.com.mx/acura/rlx/',
                 'https://autos.mercadolibre.com.mx/mazda/rx-8/',
                 'https://autos.mercadolibre.com.mx/dodge/ram/',
                 'https://autos.mercadolibre.com.mx/dodge/ram-1500/',
                 'https://autos.mercadolibre.com.mx/dodge/ram-2500/',
                 'https://autos.mercadolibre.com.mx/dodge/ram-3500/',
                 'https://autos.mercadolibre.com.mx/dodge/ram-charger/',
                 'https://autos.mercadolibre.com.mx/dodge/ram-wagon/',
                 'https://autos.mercadolibre.com.mx/land-rover/range-rover/',
                 'https://autos.mercadolibre.com.mx/land-rover/range-rover-sport/',
                 'https://autos.mercadolibre.com.mx/ford/ranger/',
                 'https://autos.mercadolibre.com.mx/buick/regal/',
                 'https://autos.mercadolibre.com.mx/jeep/renegade/',
                 'https://autos.mercadolibre.com.mx/honda/ridgeline/',
                 'https://autos.mercadolibre.com.mx/kia/rio/',
                 'https://autos.mercadolibre.com.mx/smart-/roadster/',
                 'https://autos.mercadolibre.com.mx/isuzu/rodeo/',
                 'https://autos.mercadolibre.com.mx/nissan/rogue/',
                 'https://autos.mercadolibre.com.mx/volkswagen/routan/',
                 'https://autos.mercadolibre.com.mx/jeep/rubicon/',
                 'https://autos.mercadolibre.com.mx/toyota/rush/',
                 'https://autos.mercadolibre.com.mx/chevrolet/s-10/',
                 'https://autos.mercadolibre.com.mx/suzuki/s-cross/',
                 'https://autos.mercadolibre.com.mx/satur/s-series/',
                 'https://autos.mercadolibre.com.mx/jaguar/s-type/',
                 'https://autos.mercadolibre.com.mx/volvo/s40/',
                 'https://autos.mercadolibre.com.mx/volvo/s60/',
                 'https://autos.mercadolibre.com.mx/volvo/s80/',
                 'https://autos.mercadolibre.com.mx/volvo/s90/',
                 'https://autos.mercadolibre.com.mx/nissan/se-r/',
                 'https://autos.mercadolibre.com.mx/jac/sei2/',
                 'https://autos.mercadolibre.com.mx/jac/sei3/',
                 'https://autos.mercadolibre.com.mx/cadillac/sls/',
                 'https://autos.mercadolibre.com.mx/cadillac/srx/',
                 'https://autos.mercadolibre.com.mx/ra/st/',
                 'https://autos.mercadolibre.com.mx/cadillac/sts/',
                 'https://autos.mercadolibre.com.mx/suzuki/sx4/',
                 'https://autos.mercadolibre.com.mx/ford/sable/',
                 'https://autos.mercadolibre.com.mx/renault/safrane/',
                 'https://autos.mercadolibre.com.mx/suzuki/samurai/',
                 'https://autos.mercadolibre.com.mx/renault/sandero/',
                 'https://autos.mercadolibre.com.mx/hyundai/santa-fe/',
                 'https://autos.mercadolibre.com.mx/savana/',
                 'https://autos.mercadolibre.com.mx/volkswagen/saveiro/',
                 'https://autos.mercadolibre.com.mx/volkswagen/saveiro-cross/',
                 'https://autos.mercadolibre.com.mx/renault/scala/',
                 'https://autos.mercadolibre.com.mx/renault/scenic/',
                 'https://autos.mercadolibre.com.mx/chrysler/sebring/',
                 'https://autos.mercadolibre.com.mx/nissan/sentra/',
                 'https://autos.mercadolibre.com.mx/toyota/sequoia/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-1/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-2/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-3/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-4/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-5/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-6/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-7/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-8/',
                 'https://autos.mercadolibre.com.mx/bmw/serie-m/',
                 'https://autos.mercadolibre.com.mx/audi/serie-rs/',
                 'https://autos.mercadolibre.com.mx/audi/serie-s/',
                 'https://autos.mercadolibre.com.mx/cadillac/seville/',
                 'https://autos.mercadolibre.com.mx/chrysler/shadow/',
                 'https://autos.mercadolibre.com.mx/volkswagen/sharan/',
                 'https://autos.mercadolibre.com.mx/toyota/sienna/',
                 'https://autos.mercadolibre.com.mx/sierra/',
                 'https://autos.mercadolibre.com.mx/chevrolet/silverado/',
                 'https://autos.mercadolibre.com.mx/toyota/solara/',
                 'https://autos.mercadolibre.com.mx/pontiac/solstice/',
                 'https://autos.mercadolibre.com.mx/hyundai/sonata/',
                 'https://autos.mercadolibre.com.mx/chevrolet/sonic/',
                 'https://autos.mercadolibre.com.mx/gmc/sanoma/',
                 'https://autos.mercadolibre.com.mx/chevrolet/sonora/',
                 'https://autos.mercadolibre.com.mx/kia/sorento/',
                 'https://autos.mercadolibre.com.mx/kia/soul/',
                 'https://autos.mercadolibre.com.mx/mitsubishi/space-star/',
                 'https://autos.mercadolibre.com.mx/chevrolet/spark/',
                 'https://autos.mercadolibre.com.mx/alfa-romeo/spider/',
                 'https://autos.mercadolibre.com.mx/chrysler/spirit/',
                 'https://autos.mercadolibre.com.mx/volkswagen/sport-van/',
                 'https://autos.mercadolibre.com.mx/kia/sportage/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/sprinter/',
                 'https://autos.mercadolibre.com.mx/renault/stepway/',
                 'https://autos.mercadolibre.com.mx/fiat/stilo/',
                 'https://autos.mercadolibre.com.mx/fiat/strada/',
                 'https://autos.mercadolibre.com.mx/stratus/',
                 'https://autos.mercadolibre.com.mx/chevrolet/suburban/',
                 'https://autos.mercadolibre.com.mx/pontiac/sunfire/',
                 'https://autos.mercadolibre.com.mx/suzuki/swift/',
                 'https://autos.mercadolibre.com.mx/toyota/t100/',
                 'https://autos.mercadolibre.com.mx/mg/tf/',
                 'https://autos.mercadolibre.com.mx/acura/tl/',
                 'https://autos.mercadolibre.com.mx/acura/tlx/',
                 'https://autos.mercadolibre.com.mx/acura/tsx/',
                 'https://autos.mercadolibre.com.mx/audi/tt/',
                 'https://autos.mercadolibre.com.mx/toyota/tacoma/',
                 'https://autos.mercadolibre.com.mx/chevrolet/tahoe/',
                 'https://autos.mercadolibre.com.mx/ford/taurus/',
                 'https://autos.mercadolibre.com.mx/toyota/tercel/',
                 'https://autos.mercadolibre.com.mx/gmc/terrain/',
                 'https://autos.mercadolibre.com.mx/ford/thunderbird/',
                 'https://autos.mercadolibre.com.mx/tigra/',
                 'https://autos.mercadolibre.com.mx/volkswagen/tiguan/',
                 'https://autos.mercadolibre.com.mx/nissan/tiida/',
                 'https://autos.mercadolibre.com.mx/nissan/titan/',
                 'https://autos.mercadolibre.com.mx/seat/toledo/',
                 'https://autos.mercadolibre.com.mx/ford/topaz/',
                 'https://autos.mercadolibre.com.mx/chevrolet/tornado/',
                 'https://autos.mercadolibre.com.mx/pontiac/torrent/',
                 'https://autos.mercadolibre.com.mx/volkswagen/touareg/',
                 'https://autos.mercadolibre.com.mx/chrysler/town-country/',
                 'https://autos.mercadolibre.com.mx/lincoln/town-car/',
                 'https://autos.mercadolibre.com.mx/chevrolet/tracker/',
                 'https://autos.mercadolibre.com.mx/renault/trafic/',
                 'https://autos.mercadolibre.com.mx/chevrolet/trailblazer/',
                 'https://autos.mercadolibre.com.mx/pontiac/trans-am/',
                 'https://autos.mercadolibre.com.mx/pontiac/trans-sport/',
                 'https://autos.mercadolibre.com.mx/ford/transit/',
                 'https://autos.mercadolibre.com.mx/chevrolet/transport/',
                 'https://autos.mercadolibre.com.mx/volkswagen/transporter/',
                 'https://autos.mercadolibre.com.mx/chevrolet/traverse/',
                 'https://autos.mercadolibre.com.mx/chevrolet/trax/',
                 'https://autos.mercadolibre.com.mx/ford/tremor/',
                 'https://autos.mercadolibre.com.mx/subaru/tribeca/',
                 'https://autos.mercadolibre.com.mx/isuzu/trooper/',
                 'https://autos.mercadolibre.com.mx/nissan/tsubame/',
                 'https://autos.mercadolibre.com.mx/nissan/tsuru/',
                 'https://autos.mercadolibre.com.mx/nissan/tsuru-ii/',
                 'https://autos.mercadolibre.com.mx/hyundai/tucson/',
                 'https://autos.mercadolibre.com.mx/toyota/tundra/',
                 'https://autos.mercadolibre.com.mx/renault/twizy/',
                 'https://autos.mercadolibre.com.mx/fiat/uno/',
                 'https://autos.mercadolibre.com.mx/volkswagen/up/',
                 'https://autos.mercadolibre.com.mx/chevrolet/uplander/',
                 'https://autos.mercadolibre.com.mx/nissan/urvan/',
                 'https://autos.mercadolibre.com.mx/volvo/v40/',
                 'https://autos.mercadolibre.com.mx/volvo/v50/',
                 'https://autos.mercadolibre.com.mx/volvo/v60/',
                 'https://autos.mercadolibre.com.mx/volvo/v70/',
                 'https://autos.mercadolibre.com.mx/volkswagen/vw-van/',
                 'https://autos.mercadolibre.com.mx/chevrolet/vanette/',
                 'https://autos.mercadolibre.com.mx/aston-martin/vanquish/',
                 'https://autos.mercadolibre.com.mx/aston-martin/vantage/',
                 'https://autos.mercadolibre.com.mx/vectra/',
                 'https://autos.mercadolibre.com.mx/volkswagen/vento/',
                 'https://autos.mercadolibre.com.mx/chevrolet/venture/',
                 'https://autos.mercadolibre.com.mx/buick/verano/',
                 'https://autos.mercadolibre.com.mx/dodge/verna/',
                 'https://autos.mercadolibre.com.mx/nissan/versa/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/viano/',
                 'https://autos.mercadolibre.com.mx/villager/',
                 'https://autos.mercadolibre.com.mx/dodge/viper/',
                 'https://autos.mercadolibre.com.mx/dodge/vision/',
                 'https://autos.mercadolibre.com.mx/suzuki/vitara/',
                 'https://autos.mercadolibre.com.mx/mercedes-benz/vito/',
                 'https://autos.mercadolibre.com.mx/chevrolet/volt/',
                 'https://autos.mercadolibre.com.mx/chrysler/voyager/',
                 'https://autos.mercadolibre.com.mx/subaru/wrx/',
                 'https://autos.mercadolibre.com.mx/ford/windstar/',
                 'https://autos.mercadolibre.com.mx/jeep/wrangler/',
                 'https://autos.mercadolibre.com.mx/nissan/x-terra/',
                 'https://autos.mercadolibre.com.mx/nissan/x-trail/',
                 'https://autos.mercadolibre.com.mx/jaguar/x-type/',
                 'https://autos.mercadolibre.com.mx/bmw/x1/',
                 'https://autos.mercadolibre.com.mx/baic/x25/',
                 'https://autos.mercadolibre.com.mx/bmw/x3/',
                 'https://autos.mercadolibre.com.mx/bmw/x4/',
                 'https://autos.mercadolibre.com.mx/bmw/x5/',
                 'https://autos.mercadolibre.com.mx/bmw/x5-m/',
                 'https://autos.mercadolibre.com.mx/bmw/x6/',
                 'https://autos.mercadolibre.com.mx/bmw/x6-m/',
                 'https://autos.mercadolibre.com.mx/baic/x65/',
                 'https://autos.mercadolibre.com.mx/volvo/xc60/',
                 'https://autos.mercadolibre.com.mx/volvo/xc70/',
                 'https://autos.mercadolibre.com.mx/volvo/xc90/',
                 'https://autos.mercadolibre.com.mx/jaguar/xe/',
                 'https://autos.mercadolibre.com.mx/jaguar/xf/',
                 'https://autos.mercadolibre.com.mx/jaguar/xj/',
                 'https://autos.mercadolibre.com.mx/jaguar/xk/',
                 'https://autos.mercadolibre.com.mx/jaguar/xkr/',
                 'https://autos.mercadolibre.com.mx/suzuki/xl7/',
                 'https://autos.mercadolibre.com.mx/cadillac/xl/',
                 'https://autos.mercadolibre.com.mx/cadillac/xt5/',
                 'https://autos.mercadolibre.com.mx/cadillac/xts/',
                 'https://autos.mercadolibre.com.mx/subaru/xv/',
                 'https://autos.mercadolibre.com.mx/toyota/yaris/',
                 'https://autos.mercadolibre.com.mx/gmc/yukon/',
                 'https://autos.mercadolibre.com.mx/bmw/z3/',
                 'https://autos.mercadolibre.com.mx/bmw/z4/',
                 'https://autos.mercadolibre.com.mx/acura/zdx/',
                 'https://autos.mercadolibre.com.mx/mg/zr/',
                 'https://autos.mercadolibre.com.mx/mg/zt/',
                 'https://autos.mercadolibre.com.mx/zafira/',
                 'https://autos.mercadolibre.com.mx/lincoln/zephyr/']



    def parse(self, response):
        liste = response.xpath("//div/section/ol/li/div/a/@href").extract()
        for url in liste:
            if url is not None:
                #print (url)
                yield scrapy.Request(url=url, callback=self.details)
        page_suiv = response.xpath("//li[@class='pagination__next']/a/@href").extract_first()
        if page_suiv is not None:
            print(("------------------------>",page_suiv))
            yield scrapy.Request(url=page_suiv,callback=self.parse)
    def correct(self,champ):

        return str(champ).replace('\r', '').replace('\n', '').replace('\t', '').replace(';', '').replace('\"', '').replace('None','').strip()

    def extraction_tel(self,numero):
        tel11=str(numero)
        tel111=re.findall("([0-9]+)",tel11)
        tel1=""
        for tel1111 in tel111:
            tel1=str(tel1)+str(tel1111)
        if len(tel1)==12 and (tel1[0]+tel1[1])=="52":
            tel1=tel1[2:]
                
        return str(tel1)

    def details(self, response):
        item = MercadolibreItem()
        
        id_annonce=response.xpath("//input[@name='itemId']/@value")
        if id_annonce:
            id_annonce=id_annonce.extract_first()
        else:
            id_annonce=''

        mini_site=response.xpath("//a[@class='seller-info-link']/@href")
        if mini_site:
            mini_site=mini_site.extract_first()

            id_garage_etape1=mini_site.split("_CustId_")
            id_garage_etape2=id_garage_etape1[1].split("_")
            id_garage=id_garage_etape2[0]



        else:
            mini_site=''
            id_garage=''

        nom_garage=response.xpath("//p[@class='disclaimer']/text()")
        if nom_garage:
            nom_garage=nom_garage.extract_first()
        else:
            nom_garage=''

        marque = response.xpath("//nav/div/ul/li[3]/a/text()")
        if marque:
            marque= marque.extract()[-1].strip()
        else:
            marque=''

        model = response.xpath("//nav/div/ul/li[4]/a/text()")
        if model:
            model=model.extract_first()
        else:
            model=''

        titre = response.xpath("//section/div/header/h1/text()")
        if titre:
            titre=titre.extract_first()
        else:
            titre=''

        type_annonceur=response.xpath("//p[@class='card-title']/text()")
        if type_annonceur:
            type_annonceur=type_annonceur.extract_first()
            if type_annonceur=='Información de la agencia':
                type_annonceur='Y'
            elif type_annonceur=='Información sobre el vendedor':
                type_annonceur='N'


        else:
            type_annonceur=''


        tel = response.xpath("//div/section/p[contains(.,'Teléfono')]/following-sibling::p/span/span/text()")
        if tel:
            tel=tel.extract()
        else:
            tel=''

        contact_nom = response.xpath(
            "//div/section/p[contains(.,'Nombre')]/following-sibling::p/span/text()")
        if contact_nom:
            contact_nom=contact_nom.extract_first()
        else:
            contact_nom=''

        emplacement =response.xpath("//div[@class='location-info'][contains(.,'El vehículo')]/text()") 
      #ancien xpath  #response.xpath("//div/section/p[contains(.,'Ubicación del vehículo')]/following-sibling::p/span/text()")
        ville=''
        departement=''
        province=''
        if emplacement:
            emplacement=emplacement.extract()[1].strip().replace("El vehículo está en ","")
            details_emplacement=emplacement.split("-")
            if len(details_emplacement)==3:
                ville=details_emplacement[0]
                departement=details_emplacement[1]
                province=details_emplacement[2]
            elif len(details_emplacement)==2:
                ville=details_emplacement[0]
                province=details_emplacement[1]
            elif len(details_emplacement)==1:
                province=details_emplacement[0]




        else:
            emplacement=''

        prix_chifre = response.xpath("//div/section/div/fieldset/span/span[2]/text()")

        if prix_chifre:
            prix_chifre=prix_chifre.extract_first()
        else:
            prix_chifre=''

        prix_symbol = response.xpath("//div/section/div/fieldset/span/span[1]/text()")
        if prix_symbol:
            prix_symbol=prix_symbol.extract_first()
        else:
            prix_symbol=''            
       
        if (prix_chifre and prix_symbol) is not None:
            if 'U' in prix_symbol or 'S' in prix_symbol or "u" in prix_symbol or "s" in prix_symbol:
                prix = str(prix_chifre.replace(",",""))+' USD'
                #prix = int(prix_chifre.replace(",",""))#ancien condition
            else:
                prix = str(prix_chifre.replace(",",""))+' MXN'
                #prix = int(int(prix_chifre.replace(",",""))/19)#ancien condition

        annee_kilometrage = response.xpath("//div/section/div/article/dl/dd/text()")
        if annee_kilometrage:
            annee_kilometrage=annee_kilometrage.extract()
        else:
            annee_kilometrage=''

        type_Vo = response.xpath(
            "//div/section/ul/li/strong[contains('Tipo',.)]/following-sibling::span/text()")
        if type_Vo:
            type_Vo=type_Vo.extract_first()
        else:
            type_Vo=''

        motor = response.xpath(
            "//div/section/ul/li/strong[contains('Motor',.)]/following-sibling::span/text()")
        if motor:
            motor=motor.extract_first()
        else:
            motor=''

        transmision = response.xpath(
            "//div/section/ul/li/strong[contains(.,'Transmisión')]/following-sibling::span/text()")
        if transmision:
            transmision=transmision.extract_first()
        else:
            transmision=''

        color = response.xpath(
            "//div/section/ul/li/strong[contains('Color',.)]/following-sibling::span/text()")
        if color:
            color=color.extract_first()
        else:
            color=''
        #color_caoutchouc = response.xpath(
        #    "//div/section/ul/li/strong[contains(.,'Color de engomado')]/following-sibling::span/text()").extract_first()

        #prop_uniq = response.xpath(
         #   "//div/section/ul/li/strong[contains('Único dueño',.)]/following-sibling::span/text()").extract_first()

        type_carb = response.xpath(
            "//div/section/ul/li/strong[contains(.,'Tipo de combustible')]/following-sibling::span/text()")
        if type_carb:
            type_carb=type_carb.extract_first()
        else:
            type_carb=''

        nb_port = response.xpath(
            "//div/section/ul/li/strong[contains(.,'Puertas')]/following-sibling::span/text()")
        if nb_port:
            nb_port=nb_port.extract_first()
        else:
            nb_port=''

        puissance = response.xpath(
            "//div/section/ul/li/strong[contains(.,'Potencia')]/following-sibling::span/text()")
        if puissance:
            puissance=puissance.extract_first()
        else:
            puissance=''

        plaque = response.xpath(
            "//div/section/ul/li/strong[contains(.,'Placa')]/following-sibling::span/text()")
        if plaque:
            plaque=plaque.extract_first()
        else:
            plaque=''
        # Dimensiones y capacidades*********************
        #hauteur = response.xpath("//div/ul/li[contains(.,'Altura')]/span/text()").extract_first()

        nb_personne = response.xpath("//div/section/div/div/div/div/ul/li[contains(.,'Capacidad de personas')]/span/text()")
        if nb_personne:
            nb_personne=nb_personne.extract_first()
        else:
            nb_personne=''          
        #large = response.xpath("//div/ul/li[contains(.,'Largo')]/span/text()").extract_first()
        #largeur = response.xpath("//div/ul/li[contains(.,'Ancho')]/span/text()").extract_first()
        #distance_axe = response.xpath("//div/ul/li[contains(.,'Distancia entre ejes')]/span/text()").extract_first()
        #cp_reservoir = response.xpath("//div/ul/li[contains(.,'Capacidad del tanque')]/span/text()").extract_first()

        # Motor y Performance************************
        cylindre = response.xpath("//div/ul/li[contains(.,'Cilindrada')]/span/text()")
        if cylindre:
            cylindre=cylindre.extract_first()
            if 'cc' in str(cylindre):
                cylindre=str(cylindre).replace('cc','')
        else:
            cylindre=''
        #valve_cylind = response.xpath("//div/ul/li[contains(.,'Válvulas por cilindro')]/span/text()").extract_first()
        
        # Dirección y transmisión*************************
        #direction = response.xpath("//div/ul/li[contains(.,'Dirección')]/span/text()").extract_first()
        #control_traction = response.xpath("//div/ul/li[contains(.,'Control de tracción')]/span/text()").extract_first()
        
        nb_vitesse = response.xpath("//div/ul/li[contains(.,'Numero de velocidades')]/span/text()")
        if nb_vitesse:
            nb_vitesse=nb_vitesse.extract_first()
        else:
            nb_vitesse=''
        # description******************************************

        desc = response.xpath("//div/section/div/div[@class='item-description__text']/p/text()")
        if desc:
            desc=desc.extract()
        else:
            desc=''
        image=response.xpath('//figure/a[@class="gallery-trigger "]/@data-imgindex').extract()
           #taille de dernier  image
        size_image=response.xpath('//figure/a[@class="gallery-trigger "]/@data-size').extract()[-1]
        if size_image=="":
            nbr_image=0
        elif size_image != "" and image ==[]:
            nbr_image=1

        else:
            nbr_image=int(image[-1])+1
            
 

        item['SITE'] = "autos.mercadolibre.com.mx"
        item['ANNONCE_LINK'] = self.correct(response.url)
        item['MARQUE'] = self.correct(marque)
        item['MODELE'] = self.correct(model)

        item['NOM'] = self.correct(titre)

#********************en cas champ de telef mais plusieur  numero separer par / ****************************************************
        if len(tel)==1 and "/" in str(tel[0]):
            nbr_telf=tel[0].split("/")
            if len(nbr_telf)==1:

                item['TELEPHONE']=self.extraction_tel(nbr_telf[0])
            elif len(nbr_telf)==2:
                item['TELEPHONE']=self.extraction_tel(nbr_telf[0])

                item['TELEPHONE_2']=self.extraction_tel(nbr_telf[1])
            elif len(nbr_telf)==3:
                item['TELEPHONE']=self.extraction_tel(nbr_telf[0])
                item['TELEPHONE_2']=self.extraction_tel(nbr_telf[1])
                item['TELEPHONE_3']=self.extraction_tel(nbr_telf[2])
            else:
                item['TELEPHONE']=self.extraction_tel(nbr_telf[0])
                item['TELEPHONE_2']=self.extraction_tel(nbr_telf[1])
                item['TELEPHONE_3']=self.extraction_tel(nbr_telf[2])

                item['TELEPHONE_4']=self.extraction_tel(nbr_telf[3])



#en cas de 1 numero telef---------------------------------------------------------

        elif len(tel)==1:
                item['TELEPHONE']=self.extraction_tel(tel[0])

#********************en cas 2 numero tele ****************************************************
        elif len(tel)==2:
                item['TELEPHONE']=self.extraction_tel(tel[0])
                item['TELEPHONE_2']=self.extraction_tel(tel[1])


#********************en cas 3 numero tele ****************************************************

#les boucle et le variable 333 et 3333 c est pour concatiner le numero apre eliminiation de ( et )
        elif len(tel)==3:
                item['TELEPHONE']=self.extraction_tel(tel[0])
                item['TELEPHONE_2']=self.extraction_tel(tel[1])
                item['TELEPHONE_3']=self.extraction_tel(tel[2])

#en cas de 4 numerooooo***************************************

        elif len(tel)==4:
                item['TELEPHONE']=self.extraction_tel(tel[0])
                item['TELEPHONE_2']=self.extraction_tel(tel[1])
                item['TELEPHONE_3']=self.extraction_tel(tel[2])
                item['TELEPHONE_4']=self.extraction_tel(tel[3])
        else:
            item['TELEPHONE']=""
            item['TELEPHONE_2'] =""
            item['TELEPHONE_3'] =""
            item['TELEPHONE_4'] =""


#********************************************************************


        item['CONTACT'] = self.correct(contact_nom)
        item['ADRESSE'] = self.correct(emplacement)
        item['PRIX'] = self.correct(prix).replace(',','')
        if len(annee_kilometrage) ==2:
            item['ANNEE'] = self.correct(annee_kilometrage[0])
            item['KM'] = self.correct(annee_kilometrage[1].replace('km','').replace(',',''))
        elif len(annee_kilometrage) ==1 and "km" in annee_kilometrage:
            item['KM'] = self.correct(annee_kilometrage[0].replace('km','').replace(',',''))
            item['ANNEE'] =""
        elif len(annee_kilometrage) ==1 and "km" not in annee_kilometrage:
            item['ANNEE'] = self.correct(annee_kilometrage[0])
            item['KM'] = ""

        else:
            item['ANNEE'] =""
            item['KM'] = ""


        item['CARROSSERIE'] = self.correct(type_Vo)
        #item['motor'] = self.correct(motor)
        item['BOITE'] = self.correct(transmision)
        item['COULEUR'] = self.correct(color)
        #item['prop_uniq'] = self.correct(prop_uniq)
        item['CARBURANT'] = self.correct(type_carb)
        item['PORTE'] = self.correct(nb_port)
        item['PUISSANCE'] = self.correct(puissance)
        #item['plaque'] = self.correct(plaque)
        #item['color_caoutchouc'] = self.correct(color_caoutchouc)
        # Dimensiones y capacidades*********************
        #item['hauteur'] = self.correct(hauteur)
        item['PLACE'] = self.correct(nb_personne)
        #item['large'] = self.correct(large)
        #item['largeur'] = self.correct(largeur)
        #item['distance_axe'] = self.correct(distance_axe)
        #item['cp_reservoir'] = self.correct(cp_reservoir)
        # Motor y Performance************************

        item['CYLINDRE'] = self.correct(cylindre)
        #item['valve_cylind'] = self.correct(valve_cylind)
        # Dirección y transmisión*************************

        #item['direction'] = self.correct(direction)
        #item['control_traction'] = self.correct(control_traction)
        item['NB_VITESSE'] = self.correct(nb_vitesse)

        # description******************************************

        item['OPTIONS'] = self.correct(desc).replace('[','').replace(']','')
        item['ID_CLIENT']=self.correct(id_annonce)
        item['VILLE']=self.correct(ville)
        item['DEPARTEMENT']=self.correct(departement)
        item['PROVINCE']=self.correct(province)
        item['TYPE']=self.correct(type_annonceur)
        item['GARAGE_ID']=self.correct(id_garage)
        item['GARAGE_NAME']=self.correct(nom_garage)
        item['minisite']=self.correct(mini_site)
        item['PHOTO']=self.correct(nbr_image)

        yield item







