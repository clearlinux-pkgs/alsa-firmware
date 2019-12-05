#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : alsa-firmware
Version  : 1.2.1
Release  : 5
URL      : https://www.alsa-project.org/files/pub/firmware/alsa-firmware-1.2.1.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/firmware/alsa-firmware-1.2.1.tar.bz2
Summary  : ALSA firmware package
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: alsa-firmware-data = %{version}-%{release}
Requires: alsa-firmware-license = %{version}-%{release}

%description
GENERAL
=======
This package contains the firmware binaries for each loader program
included in alsa-tools package.  The firmware data can be used by each
ALSA firmware loader program like vxloader, or passed through the
hotplug firmware-loading mechanism.

%package data
Summary: data components for the alsa-firmware package.
Group: Data

%description data
data components for the alsa-firmware package.


%package license
Summary: license components for the alsa-firmware package.
Group: Default

%description license
license components for the alsa-firmware package.


%prep
%setup -q -n alsa-firmware-1.2.1
cd %{_builddir}/alsa-firmware-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575546236
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1575546236
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-firmware
cp %{_builddir}/alsa-firmware-1.2.1/COPYING %{buildroot}/usr/share/package-licenses/alsa-firmware/9db6e6f4189b7101178eef598c9985910e51456d
cp %{_builddir}/alsa-firmware-1.2.1/aica/license.txt %{buildroot}/usr/share/package-licenses/alsa-firmware/f1ed3062fa64763c2e60ce4cd36a39117d44ee3c
%make_install
## install_append content
mv %{buildroot}/lib/* %{buildroot}/usr/lib/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/aica_firmware.bin
/usr/lib/asihpi/dsp5000.bin
/usr/lib/asihpi/dsp6200.bin
/usr/lib/asihpi/dsp6205.bin
/usr/lib/asihpi/dsp6400.bin
/usr/lib/asihpi/dsp6600.bin
/usr/lib/asihpi/dsp8700.bin
/usr/lib/asihpi/dsp8900.bin
/usr/lib/cs46xx/ba1
/usr/lib/cs46xx/cwc4630
/usr/lib/cs46xx/cwcasync
/usr/lib/cs46xx/cwcbinhack
/usr/lib/cs46xx/cwcdma
/usr/lib/cs46xx/cwcsnoop
/usr/lib/ctefx-desktop.bin
/usr/lib/ctefx-r3di.bin
/usr/lib/ctefx.bin
/usr/lib/ctspeq.bin
/usr/lib/digiface_firmware.bin
/usr/lib/digiface_firmware_rev11.bin
/usr/lib/ea/3g_asic.fw
/usr/lib/ea/darla20_dsp.fw
/usr/lib/ea/darla24_dsp.fw
/usr/lib/ea/echo3g_dsp.fw
/usr/lib/ea/gina20_dsp.fw
/usr/lib/ea/gina24_301_asic.fw
/usr/lib/ea/gina24_301_dsp.fw
/usr/lib/ea/gina24_361_asic.fw
/usr/lib/ea/gina24_361_dsp.fw
/usr/lib/ea/indigo_dj_dsp.fw
/usr/lib/ea/indigo_djx_dsp.fw
/usr/lib/ea/indigo_dsp.fw
/usr/lib/ea/indigo_io_dsp.fw
/usr/lib/ea/indigo_iox_dsp.fw
/usr/lib/ea/layla20_asic.fw
/usr/lib/ea/layla20_dsp.fw
/usr/lib/ea/layla24_1_asic.fw
/usr/lib/ea/layla24_2A_asic.fw
/usr/lib/ea/layla24_2S_asic.fw
/usr/lib/ea/layla24_dsp.fw
/usr/lib/ea/loader_dsp.fw
/usr/lib/ea/mia_dsp.fw
/usr/lib/ea/mona_2_asic.fw
/usr/lib/ea/mona_301_1_asic_48.fw
/usr/lib/ea/mona_301_1_asic_96.fw
/usr/lib/ea/mona_301_dsp.fw
/usr/lib/ea/mona_361_1_asic_48.fw
/usr/lib/ea/mona_361_1_asic_96.fw
/usr/lib/ea/mona_361_dsp.fw
/usr/lib/emu/audio_dock.fw
/usr/lib/emu/emu0404.fw
/usr/lib/emu/emu1010_notebook.fw
/usr/lib/emu/emu1010b.fw
/usr/lib/emu/hana.fw
/usr/lib/emu/micro_dock.fw
/usr/lib/ess/maestro3_assp_kernel.fw
/usr/lib/ess/maestro3_assp_minisrc.fw
/usr/lib/korg/k1212.dsp
/usr/lib/mixart/miXart8.elf
/usr/lib/mixart/miXart8.xlx
/usr/lib/mixart/miXart8AES.xlx
/usr/lib/multiface_firmware.bin
/usr/lib/multiface_firmware_rev11.bin
/usr/lib/pcxhr/b321_512.b56
/usr/lib/pcxhr/d321_512.d56
/usr/lib/pcxhr/dspb1222e.b56
/usr/lib/pcxhr/dspb1222hr.b56
/usr/lib/pcxhr/dspb882e.b56
/usr/lib/pcxhr/dspb882hr.b56
/usr/lib/pcxhr/dspb924.b56
/usr/lib/pcxhr/dspd1222.d56
/usr/lib/pcxhr/dspd222.d56
/usr/lib/pcxhr/dspd882.d56
/usr/lib/pcxhr/dspe882.e56
/usr/lib/pcxhr/dspe924.e56
/usr/lib/pcxhr/e321_512.e56
/usr/lib/pcxhr/xc_1_882.dat
/usr/lib/pcxhr/xi_1_882.dat
/usr/lib/pcxhr/xlxc1222e.dat
/usr/lib/pcxhr/xlxc1222hr.dat
/usr/lib/pcxhr/xlxc222.dat
/usr/lib/pcxhr/xlxc882e.dat
/usr/lib/pcxhr/xlxc882hr.dat
/usr/lib/pcxhr/xlxc924.dat
/usr/lib/pcxhr/xlxint.dat
/usr/lib/rpm_firmware.bin
/usr/lib/sb16/alaw_main.csp
/usr/lib/sb16/ima_adpcm_capture.csp
/usr/lib/sb16/ima_adpcm_init.csp
/usr/lib/sb16/ima_adpcm_playback.csp
/usr/lib/sb16/mulaw_main.csp
/usr/lib/turtlebeach/msndinit.bin
/usr/lib/turtlebeach/msndperm.bin
/usr/lib/turtlebeach/pndsperm.bin
/usr/lib/turtlebeach/pndspini.bin
/usr/lib/vx/bd56002.boot
/usr/lib/vx/bd563s3.boot
/usr/lib/vx/bd563v2.boot
/usr/lib/vx/bx_1_vp4.b56
/usr/lib/vx/bx_1_vxp.b56
/usr/lib/vx/l_1_v22.d56
/usr/lib/vx/l_1_vp4.d56
/usr/lib/vx/l_1_vx2.d56
/usr/lib/vx/l_1_vxp.d56
/usr/lib/vx/x1_1_vp4.xlx
/usr/lib/vx/x1_1_vx2.xlx
/usr/lib/vx/x1_1_vxp.xlx
/usr/lib/vx/x1_2_v22.xlx
/usr/lib/yamaha/ds1_ctrl.fw
/usr/lib/yamaha/ds1_dsp.fw
/usr/lib/yamaha/ds1e_ctrl.fw
/usr/lib/yamaha/yss225_registers.bin

%files data
%defattr(-,root,root,-)
/usr/share/alsa/firmware/hdsploader/digiface_firmware.bin
/usr/share/alsa/firmware/hdsploader/digiface_firmware_rev11.bin
/usr/share/alsa/firmware/hdsploader/multiface_firmware.bin
/usr/share/alsa/firmware/hdsploader/multiface_firmware_rev11.bin
/usr/share/alsa/firmware/hdsploader/rpm_firmware.bin
/usr/share/alsa/firmware/mixartloader/miXart.conf
/usr/share/alsa/firmware/mixartloader/miXart8.elf
/usr/share/alsa/firmware/mixartloader/miXart8.xlx
/usr/share/alsa/firmware/mixartloader/miXart8AES.xlx
/usr/share/alsa/firmware/pcxhrloader/b321_512.b56
/usr/share/alsa/firmware/pcxhrloader/d321_512.d56
/usr/share/alsa/firmware/pcxhrloader/dspb1222e.b56
/usr/share/alsa/firmware/pcxhrloader/dspb1222hr.b56
/usr/share/alsa/firmware/pcxhrloader/dspb882e.b56
/usr/share/alsa/firmware/pcxhrloader/dspb882hr.b56
/usr/share/alsa/firmware/pcxhrloader/dspb924.b56
/usr/share/alsa/firmware/pcxhrloader/dspd1222.d56
/usr/share/alsa/firmware/pcxhrloader/dspd222.d56
/usr/share/alsa/firmware/pcxhrloader/dspd882.d56
/usr/share/alsa/firmware/pcxhrloader/dspe882.e56
/usr/share/alsa/firmware/pcxhrloader/dspe924.e56
/usr/share/alsa/firmware/pcxhrloader/e321_512.e56
/usr/share/alsa/firmware/pcxhrloader/pcxhr.conf
/usr/share/alsa/firmware/pcxhrloader/pcxhr0.conf
/usr/share/alsa/firmware/pcxhrloader/pcxhr1.conf
/usr/share/alsa/firmware/pcxhrloader/pcxhr2.conf
/usr/share/alsa/firmware/pcxhrloader/pcxhr3.conf
/usr/share/alsa/firmware/pcxhrloader/pcxhr4.conf
/usr/share/alsa/firmware/pcxhrloader/pcxhr5.conf
/usr/share/alsa/firmware/pcxhrloader/xc_1_882.dat
/usr/share/alsa/firmware/pcxhrloader/xi_1_882.dat
/usr/share/alsa/firmware/pcxhrloader/xlxc1222e.dat
/usr/share/alsa/firmware/pcxhrloader/xlxc1222hr.dat
/usr/share/alsa/firmware/pcxhrloader/xlxc222.dat
/usr/share/alsa/firmware/pcxhrloader/xlxc882e.dat
/usr/share/alsa/firmware/pcxhrloader/xlxc882hr.dat
/usr/share/alsa/firmware/pcxhrloader/xlxc924.dat
/usr/share/alsa/firmware/pcxhrloader/xlxint.dat
/usr/share/alsa/firmware/usx2yloader/tascam_loader.ihx
/usr/share/alsa/firmware/usx2yloader/us122.conf
/usr/share/alsa/firmware/usx2yloader/us122.prepad
/usr/share/alsa/firmware/usx2yloader/us122.rbt
/usr/share/alsa/firmware/usx2yloader/us122fw.ihx
/usr/share/alsa/firmware/usx2yloader/us224.conf
/usr/share/alsa/firmware/usx2yloader/us224.prepad
/usr/share/alsa/firmware/usx2yloader/us224.rbt
/usr/share/alsa/firmware/usx2yloader/us224fw.ihx
/usr/share/alsa/firmware/usx2yloader/us428.conf
/usr/share/alsa/firmware/usx2yloader/us428.prepad
/usr/share/alsa/firmware/usx2yloader/us428.rbt
/usr/share/alsa/firmware/usx2yloader/us428fw.ihx
/usr/share/alsa/firmware/vxloader/bd56002.boot
/usr/share/alsa/firmware/vxloader/bd563s3.boot
/usr/share/alsa/firmware/vxloader/bd563v2.boot
/usr/share/alsa/firmware/vxloader/bx_1_vp4.b56
/usr/share/alsa/firmware/vxloader/bx_1_vxp.b56
/usr/share/alsa/firmware/vxloader/l_1_v22.d56
/usr/share/alsa/firmware/vxloader/l_1_vp4.d56
/usr/share/alsa/firmware/vxloader/l_1_vx2.d56
/usr/share/alsa/firmware/vxloader/l_1_vxp.d56
/usr/share/alsa/firmware/vxloader/vx222.conf
/usr/share/alsa/firmware/vxloader/vxboard.conf
/usr/share/alsa/firmware/vxloader/vxp440.conf
/usr/share/alsa/firmware/vxloader/vxpocket.conf
/usr/share/alsa/firmware/vxloader/x1_1_vp4.rbt
/usr/share/alsa/firmware/vxloader/x1_1_vx2.rbt
/usr/share/alsa/firmware/vxloader/x1_1_vxp.rbt
/usr/share/alsa/firmware/vxloader/x1_2_v22.rbt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-firmware/9db6e6f4189b7101178eef598c9985910e51456d
/usr/share/package-licenses/alsa-firmware/f1ed3062fa64763c2e60ce4cd36a39117d44ee3c
