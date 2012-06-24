#
# TODO: for now it doesn`t build...could anyone fix it?
Summary:	GUI for htb.init script with XML data storage
Summary(pl):	Graficzny interfejs dla skryptu htb.init z danymi przechowywanymi w XML-u
Name:		khtb
Version:	0.2
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/khtb/%{name}-%{version}.tar.gz
# Source0-md5:	ff1ed8611dd82347922f07028d03f6ad
URL:		http://sourceforge.net/projects/khtb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KHtb is a GUI for htb.init script with XML data storage. It can
import-export htb.init tree. Can be used to edit remote htb.init tree
(in the future).

%description -l pl
KHtb to graficzny interfejs u�ytkownika do skryptu htb.init z
przechowywaniem danych w formacie XML. Potrafi importowa� i
eksportowa� drzewo htb.init. Mo�e by� u�ywany do modyfikowania
zdalnych drzew htb.init (w przysz�o�ci).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -Isrc"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
