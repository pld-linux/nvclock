Summary:	nvidia overclock utility
Summary(pl):	Narzêdzie do podkrêcania kart nvidia
Name:		nvclock
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.evil3d.net/pub/Evil3D/nvclock/%{name}%{version}.tar.gz
URL:		http://www.evil3d.net/products/nvclock/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_sbindir}

%description
This program allows you to overclock your nvidia card under linux.
Warning! It can burn your graphics card!

%description -l pl
Ten program pozwala Ci na podkrêcanie Twojej karty graficznej NVidia
pod Linuksem. Uwaga! Mo¿e on spaliæ twoj± kartê graficzn±!

%package gtk
Summary:	GTK frontend for nvclock
Summary(pl):	Interfejs GTK dla nvclock
Group:		Applications/System

%description gtk
GTK frontend for nvclock.

%description gtk -l pl
Interfejs GTK dla nvclock.

%prep
%setup -q -n %{name}%{version}

%build
%configure2_13 \
	--enable-gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ABOUT AUTHORS ChangeLog FAQ README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/nvclock

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvclock_gtk
