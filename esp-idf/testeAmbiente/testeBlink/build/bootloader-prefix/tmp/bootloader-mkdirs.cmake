# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/Thierry/esp/esp-idf/components/bootloader/subproject"
  "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader"
  "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix"
  "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix/tmp"
  "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix/src/bootloader-stamp"
  "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix/src"
  "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix/src/bootloader-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix/src/bootloader-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/Thierry/Documents/THIERRY/programas/ESP-IDF/testeAmbiente/testeBlink/build/bootloader-prefix/src/bootloader-stamp${cfgdir}") # cfgdir has leading slash
endif()
