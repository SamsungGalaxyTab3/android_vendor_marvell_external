%define ver      0.0.5
%define rel      1
%define prefix   /

Summary: Advanced Linux Sound Architecture (ALSA) - Utils
Name: alsa-utils
Version: %ver
Release: %rel
Copyright: GPL
Group: System/Libraries
Source: ftp://alsa.jcu.cz/pub/utils/alsa-utils-%{ver}.tar.gz 
BuildRoot: /tmp/alsa-utils-%{ver}
Packager: Helge Jensen <slog@slog.dk>
URL: http://alsa.jcu.cz
Docdir: %{prefix}/usr/doc
Requires: alsa-lib alsa-driver
%description

Advanced Linux Sound Architecture (ALSA) - Utils

Features
========

* general
  - modularized architecture with support for 2.0 and latest 2.1 kernels
  - support for versioned and exported symbols
  - full proc filesystem support - /proc/sound
* ISA soundcards
  - support for 128k ISA DMA buffer
* mixer
  - new enhanced API for applications
  - support for unlimited number of channels
  - volume can be set in three ways (percentual (0-100), exact and decibel)
  - support for mute (and hardware mute if hardware supports it)
  - support for mixer events
    - this allows two or more applications to be synchronized
* digital audio (PCM)
  - new enhanced API for applications
  - full real duplex support
  - full duplex support for SoundBlaster 16/AWE soundcards
  - digital audio data for playback and record should be read back using
    proc filesystem
* OSS/Lite compatibility
  - full mixer compatibity
  - full PCM (/dev/dsp) compatibility

%changelog

* Mon May 28 1998 Helge Jensen <slog@slog.dk>

- Made SPEC file

%prep
%setup -n alsa-utils
%build

./configure --prefix=/usr
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin

make prefix="$RPM_BUILD_ROOT/usr" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc CHANGELOG COPYING README config.status

%{prefix}/usr/bin/*