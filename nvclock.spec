# TODO: security problem (/tmp/nvclock symlink attack possible)
Summary:	NVidia overclock utility
Summary(pl.UTF-8):	Narzędzie do podkręcania kart NVidii
Name:		nvclock
Version:	0.8b4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxhardware.org/nvclock/%{name}%{version}.tar.gz
# Source0-md5:	23f1b3ebf40f35d76d5fdac50f66ab11
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.linuxhardware.org/nvclock/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	qt-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

%description -l pl.UTF-8
Ten program pozwala na podkręcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Może on spalić kartę graficzną!

%package common
Summary:	Common files for different GUI versions of nvclock
Summary(pl.UTF-8):	Wspólne pliki dla różnych wersji GUI nvclock
Group:		Applications/System

%description common
This package provides common files for different GUI versions of
nvclock.

%description common -l pl.UTF-8
Ten pakiet dostarcza wspólne pliki dla różnych wersji interfejsu
graficznego programu nvclock.

%package gtk
Summary:	GTK+ version of nvclock
Summary(pl.UTF-8):	nvclock z interfejsem GTK+
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}

%description gtk
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

This is GTK+ version.

%description gtk -l pl.UTF-8
Ten program pozwala na podkręcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Może on spalić kartę graficzną!

To jest wersja GTK+.

%package qt
Summary:	Qt version of nvclock
Summary(pl.UTF-8):	nvclock z interfejsem Qt
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}

%description qt
This program allows you to overclock your NVidia card under linux.

Warning! It can burn your graphics card!

This is Qt version.

%description qt -l pl.UTF-8
Ten program pozwala na podkręcanie karty graficznej NVidia pod
Linuksem.

Uwaga! Może on spalić kartę graficzną!

To jest wersja Qt.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%{__perl} -pi -e 's/-lqt/-lqt-mt/' src/qt/Makefile.in

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-gtk \
	--enable-qt \
	QT_LIB_DIR=%{_libdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT AUTHORS ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/nvclock
%attr(755,root,root) %{_bindir}/smartdimmer
%{_mandir}/man1/nvclock*

%files common
%defattr(644,root,root,755)
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvclock_gtk

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvclock_qt
